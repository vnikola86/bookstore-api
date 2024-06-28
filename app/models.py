from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    alias = Column(String, nullable=True)
    birth_date = Column(String, nullable=True)
    languages = Column(String, nullable=True)

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    isbn = Column(String, nullable=True)
    pages = Column(Integer, nullable=True)
    price = Column(Float, nullable=True)

    author = relationship("Author")

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    quantity = Column(Integer)
    transaction_time = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    book = relationship("Book")
