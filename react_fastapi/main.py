from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import json
from model import Books


app = FastAPI()

with open("./books.json", "r") as file:
    all_books = json.load(file)


# GET ALL BOOKS
@app.get("/")
async def books():
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"data": jsonable_encoder(all_books)}
    )


# GET ONE BOOK
@app.get("/{book_id}")
def get_one_book(book_id: int):
    book = next((book for book in all_books if book["id"] == book_id), None)
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "Book found", "book": book}
    )

## Delete a book by book_id..
@app.delete("/{book_id}")
def delete_book(book_id: int):
    
    updated_books = list(filter(lambda x : x['id'] != book_id, all_books))    
    
    with open("./books.json", "w") as file:
        json.dump(updated_books, file, indent=4)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Book deleted sucessfully"},
    )

## Add new Book..
@app.post("/")
def add_book(book:Books):
    
    new_id = max( (book['id'] for book in all_books), default=0)+1
    new_book = book.model_dump()
    new_book['id'] = new_id
    all_books.append(new_book)
    with open("./books.json", "w") as file:
        json.dump(all_books, file, indent=4)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Book Added sucessfully", "data":all_books},
    )
