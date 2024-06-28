from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter()

@router.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorBase, db: Session = Depends(database.get_db)):
    return crud.create_author(db=db, author=author)

@router.get("/authors/", response_model=list[schemas.Author])
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_authors(db=db, skip=skip, limit=limit)

@router.get("/authors/{author_id}", response_model=schemas.Author)
def read_author(author_id: int, db: Session = Depends(database.get_db)):
    db_author = crud.get_author(db=db, author_id=author_id)
    if db_author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author
