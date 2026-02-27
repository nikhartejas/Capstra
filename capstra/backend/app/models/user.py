from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    risk_profile = Column(String, nullable=False)
    capital_amount = Column(Float, nullable=False)
    experience_level = Column(String, nullable=False)
    discipline_score = Column(Integer, default=50, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    trades = relationship("Trade", back_populates="user", cascade="all, delete-orphan")
    discipline_events = relationship("DisciplineEvent", back_populates="user", cascade="all, delete-orphan")
