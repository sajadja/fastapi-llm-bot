from pydantic import BaseModel


class UserMessage(BaseModel):
    sender_id: str
    message_id: str
    text: str


class BotResponse(BaseModel):
    reply: str


class Product(BaseModel):
    id: int
    name: str
    price: float
    description: str


class ProductsData(BaseModel):
    records_count: int
    first_10_records: list[Product]
