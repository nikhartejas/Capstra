from datetime import datetime, timedelta, timezone

from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.models.trade import Trade


def detect_behavior_flags(db: Session, user_id: int, result: str, risk_percent: float, allowed_risk: float) -> dict:
    now = datetime.now(timezone.utc)
    hour_ago = now - timedelta(hours=1)
    recent_trades = (
        db.query(Trade)
        .filter(Trade.user_id == user_id, Trade.created_at >= hour_ago)
        .order_by(desc(Trade.created_at))
        .all()
    )
    last_trade = recent_trades[0] if recent_trades else None

    overtrading = len(recent_trades) >= 3
    revenge_trade = bool(last_trade and last_trade.result == "loss")
    impulse = risk_percent > allowed_risk

    warnings = []
    if overtrading:
        warnings.append("Overtrading flag: 3+ trades within 1 hour")
    if revenge_trade:
        warnings.append("Revenge trade flag: trade placed after a loss")
    if impulse:
        warnings.append("Impulse flag: risk exceeds allowed maximum")

    return {
        "overtrading": overtrading,
        "revenge_trade": revenge_trade,
        "impulse": impulse,
        "warnings": warnings,
    }
