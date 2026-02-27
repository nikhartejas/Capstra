from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.models.discipline_event import DisciplineEvent
from app.models.user import User


@dataclass
class DisciplineInput:
    risk_percent: float
    stop_loss_used: bool
    overtrading: bool
    revenge_trade: bool
    impulse: bool


def score_trade(payload: DisciplineInput) -> tuple[int, list[tuple[str, int, str]]]:
    score_delta = 0
    events: list[tuple[str, int, str]] = []

    if payload.stop_loss_used and not payload.overtrading and not payload.revenge_trade and not payload.impulse:
        score_delta += 2
        events.append(("adherence", 2, "Followed discipline rules"))

    for violated, note in [
        (payload.overtrading, "Overtrading detected"),
        (payload.revenge_trade, "Revenge trade detected"),
        (payload.impulse, "Impulse risk above allowed"),
        (not payload.stop_loss_used, "No stop loss used"),
    ]:
        if violated:
            score_delta -= 5
            events.append(("violation", -5, note))

    return score_delta, events


def apply_score(db: Session, user: User, payload: DisciplineInput) -> int:
    delta, events = score_trade(payload)
    user.discipline_score = min(100, max(0, user.discipline_score + delta))
    db.add(user)

    for event_type, event_delta, note in events:
        db.add(
            DisciplineEvent(
                user_id=user.id,
                event_type=event_type,
                delta=event_delta,
                note=note,
            )
        )
    db.commit()
    db.refresh(user)
    return user.discipline_score
