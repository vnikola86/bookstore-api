from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    alias: Optional[str] = None
    birth_date: Optional[str] = None
    languages: Optional[str] = None

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str
    author_id: int
    isbn: Optional[str] = None
    pages: Optional[int] = None
    price: Optional[float] = None

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class TransactionBase(BaseModel):
    book_id: int
    quantity: int
    transaction_time: Optional[datetime] = None

class Transaction(TransactionBase):
    id: int

    class Config:
        orm_mode = True
