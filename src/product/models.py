from ..database import Base
from sqlalchemy import Column, Integer, String, Text, REAL


class Product(Base):
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    price = Column(REAL, nullable=False)
    description = Column(Text)
