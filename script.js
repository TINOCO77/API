const addBookForm = document.getElementById("add-book-form");
const bookList = document.getElementById("book-list");

// Función para mostrar los libros en la lista
function renderBookList() {
    fetch("/books/")
        .then((response) => response.json())
        .then((data) => {
            bookList.innerHTML = "";
            for (const [bookId, book] of Object.entries(data)) {
                const li = document.createElement("li");
                li.innerHTML = `
                    <span>${book.title} - ${book.author} (${book.year})</span>
                    <button class="edit-btn" data-id="${bookId}">Editar</button>
                    <button class="delete-btn" data-id="${bookId}">Eliminar</button>
                `;
                bookList.appendChild(li);
            }
        });
}

// Función para enviar el formulario de agregar libro
function addBook(event) {
    event.preventDefault();
    const formData = new FormData(addBookForm);
    const bookData = {};
    formData.forEach((value, key) => {
        bookData[key] = value;
    });
    fetch("/books/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(bookData),
    })
        .then((response) => response.json())
        .then((data) => {
            alert(data.message);
            renderBookList();
            addBookForm.reset();
        });
}

// Función para eliminar un libro
function deleteBook(event) {
    const bookId = event.target.getAttribute("data-id");
    fetch(`/books/${bookId}`, { method: "DELETE" })
        .then((response) => response.json())
        .then((data) => {
            alert(data.message);
            renderBookList();
        });
}

// Asignar eventos a los botones
addBookForm.addEventListener("submit", addBook);
bookList.addEventListener("click", (event) => {
    if (event.target.classList.contains("delete-btn")) {
        deleteBook(event);
    }
});

// Mostrar la lista inicial de libros
renderBookList();
