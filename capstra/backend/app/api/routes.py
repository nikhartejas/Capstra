from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.agents.capital_agent import generate_capital_structure
from app.database import get_db
from app.models.discipline_event import DisciplineEvent
from app.models.trade import Trade
from app.models.user import User
from app.schemas.mentor import MentorChatIn
from app.schemas.trade import TradeLogIn
from app.schemas.user import UserCreate, UserLogin
from app.services.ai_client import AIClient
from app.services.behavior_rules import detect_behavior_flags
from app.services.discipline_engine import DisciplineInput, apply_score
from app.services.prompt_builder import build_mentor_prompt, is_blocked_message
from app.services.security import create_token, hash_password, verify_password

router = APIRouter()
ai_client = AIClient()


@router.post("/auth/signup")
def signup(payload: UserCreate, db: Session = Depends(get_db)):
    exists = db.query(User).filter(User.email == payload.email).first()
    if exists:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=payload.email,
        password_hash=hash_password(payload.password),
        risk_profile=payload.risk_profile,
        capital_amount=payload.capital_amount,
        experience_level=payload.experience_level,
        discipline_score=50,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"token": create_token(str(user.id)), "user": {"id": user.id, "email": user.email}}


@router.post("/auth/login")
def login(payload: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"token": create_token(str(user.id)), "user": {"id": user.id, "email": user.email}}


@router.get("/capital/structure/{user_id}")
def capital_structure(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return generate_capital_structure(user.risk_profile, user.capital_amount, user.experience_level)


@router.post("/trade/log")
def log_trade(payload: TradeLogIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == payload.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    allowed_risk = 0.01 if user.risk_profile == "conservative" else 0.015 if user.risk_profile == "moderate" else 0.02
    risk_per_unit = (payload.entry_price - payload.stop_loss) if payload.stop_loss else payload.entry_price * 0.03
    risk_percent = (risk_per_unit * (payload.capital_used / payload.entry_price)) / user.capital_amount

    flags = detect_behavior_flags(db, payload.user_id, payload.result, risk_percent, allowed_risk)
    trade = Trade(
        user_id=payload.user_id,
        symbol=payload.symbol,
        entry_price=payload.entry_price,
        stop_loss=payload.stop_loss,
        capital_used=payload.capital_used,
        result=payload.result,
        overtrading_flag=flags["overtrading"],
        revenge_trade_flag=flags["revenge_trade"],
        impulse_flag=flags["impulse"],
    )
    db.add(trade)
    db.commit()

    new_score = apply_score(
        db,
        user,
        DisciplineInput(
            risk_percent=risk_percent,
            stop_loss_used=payload.stop_loss is not None,
            overtrading=flags["overtrading"],
            revenge_trade=flags["revenge_trade"],
            impulse=flags["impulse"],
        ),
    )

    return {"discipline_score": new_score, "warnings": flags["warnings"]}


@router.post("/mentor/chat")
def mentor_chat(payload: MentorChatIn, db: Session = Depends(get_db)):
    if is_blocked_message(payload.message):
        raise HTTPException(status_code=400, detail="Blocked: requests for guaranteed profits or direct buy calls are not allowed.")

    user = db.query(User).filter(User.id == payload.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    violations = [
        ev.note
        for ev in db.query(DisciplineEvent)
        .filter(DisciplineEvent.user_id == user.id, DisciplineEvent.event_type == "violation")
        .order_by(DisciplineEvent.created_at.desc())
        .limit(5)
        .all()
    ]
    system_prompt = build_mentor_prompt(user, violations)
    response = ai_client.chat(system_prompt, payload.message)
    return {"response": response}


@router.get("/dashboard/{user_id}")
def dashboard(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    violations = (
        db.query(DisciplineEvent)
        .filter(DisciplineEvent.user_id == user_id, DisciplineEvent.event_type == "violation")
        .order_by(DisciplineEvent.created_at.desc())
        .limit(5)
        .all()
    )
    suggestion = "Reduce position size and enforce stop-loss on every trade."
    return {
        "capital_fitness_score": user.discipline_score,
        "recent_violations": [v.note for v in violations],
        "suggested_improvement": suggestion,
    }
