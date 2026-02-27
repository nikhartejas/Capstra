from pydantic import BaseModel


class TradeLogIn(BaseModel):
    user_id: int
    symbol: str
    entry_price: float
    stop_loss: float | None = None
    capital_used: float
    result: str
