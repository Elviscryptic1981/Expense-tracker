from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    transactions = relationship("Transaction", back_populates="owner")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, index=True)
    description = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="transactions")
