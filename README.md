# Bookstore API

This is a simple Bookstore API built with FastAPI.

## Project Structure

- `app/`: Main application folder.
  - `__init__.py`: Marks the folder as a Python package.
  - `main.py`: Entry point of the application.
  - `models.py`: SQLAlchemy models.
  - `schemas.py`: Pydantic schemas.
  - `database.py`: Database connection setup.
  - `crud.py`: CRUD operations.
  - `routers/`: Folder for routers.
    - `__init__.py`: Marks the folder as a Python package.
    - `authors.py`: Endpoints for authors.
    - `books.py`: Endpoints for books.
    - `transactions.py`: Endpoints for transactions.

## Installation

1. Install dependencies:

    pip install -r requirements.txt

2. Run the application:

    uvicorn app.main:app --reload


## Endpoints

- **Authors**
  - `POST /authors/`: Create a new author.
  - `GET /authors/`: Get a list of authors.
  - `GET /authors/{author_id}`: Get an author by ID.

- **Books**
  - `POST /books/`: Create a new book.
  - `GET /books/`: Get a list of books.
  - `GET /books/{book_id}`: Get a book by ID.

- **Transactions**
  - `POST /transactions/`: Create a new transaction.
  - `GET /transactions/`: Get a list of transactions.
  - `GET /transactions/{transaction_id}`: Get a transaction by ID.
