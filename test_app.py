import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_book():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert "Libro 1" in response.json()["title"]

def test_get_non_existing_book():
    response = client.get("/books/100")
    assert response.status_code == 404

def test_add_book():
    response = client.post("/books/", json={
        "title": "Nuevo Libro",
        "author": "Autor Nuevo",
        "year": 2023,
        "genre": "Género Nuevo"
    })
    assert response.status_code == 200
    assert "Libro agregado correctamente" in response.json()["message"]

def test_edit_book():
    response = client.put("/books/1", json={
        "title": "Libro 1 Modificado",
        "author": "Autor 1 Modificado",
        "year": 2005,
        "genre": "Género 1 Modificado"
    })
    assert response.status_code == 200
    assert "Libro editado correctamente" in response.json()["message"]

def test_edit_non_existing_book():
    response = client.put("/books/100", json={
        "title": "Libro Inexistente Modificado",
        "author": "Autor Inexistente Modificado",
        "year": 2023,
        "genre": "Género Inexistente Modificado"
    })
    assert response.status_code == 404

def test_delete_book():
    response = client.delete("/books/2")
    assert response.status_code == 200
    assert "Libro eliminado correctamente" in response.json()["message"]

def test_delete_non_existing_book():
    response = client.delete("/books/100")
    assert response.status_code == 404
