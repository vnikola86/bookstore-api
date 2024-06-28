from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from .routers import authors, books, transactions
from . import models, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(authors.router)
app.include_router(books.router)
app.include_router(transactions.router)

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <html>
        <head>
            <title>Bookstore API</title>
        </head>
        <body>
            <h1>Welcome to the Bookstore API</h1>
            <p>Use the following endpoints to interact with the API:</p>
            <ul>
                <li><a href="/docs">Interactive API Documentation</a></li>
                <li><a href="/authors/">Authors Endpoint</a></li>
                <li><a href="/books/">Books Endpoint</a></li>
                <li><a href="/transactions/">Transactions Endpoint</a></li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)