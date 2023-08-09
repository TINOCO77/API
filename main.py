from fastapi import FastAPI, HTTPException

app = FastAPI()

# Modelo de datos del libro
class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

# Datos ficticios para simular una base de datos
books_data = {
    1: Book("Libro 1", "Autor 1", 2000, "Género 1"),
    2: Book("Libro 2", "Autor 2", 2010, "Género 2"),
}

# Endpoint para obtener todos los libros
@app.get("/books/")
def get_books():
    return books_data

# Endpoint para obtener un libro por su ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in books_data:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return books_data[book_id]

# Endpoint para agregar un libro
@app.post("/books/")
def add_book(title: str, author: str, year: int, genre: str):
    book_id = max(books_data.keys()) + 1
    new_book = Book(title, author, year, genre)
    books_data[book_id] = new_book
    return {"message": "Libro agregado correctamente", "book_id": book_id}

# Endpoint para editar un libro
@app.put("/books/{book_id}")
def edit_book(book_id: int, title: str, author: str, year: int, genre: str):
    if book_id not in books_data:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    books_data[book_id].title = title
    books_data[book_id].author = author
    books_data[book_id].year = year
    books_data[book_id].genre = genre
    return {"message": "Libro editado correctamente"}

# Endpoint para eliminar un libro
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books_data:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    del books_data[book_id]
    return {"message": "Libro eliminado correctamente"}
