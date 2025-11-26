# Library Management System

A simple Library Management System built with FastAPI following Domain-Driven Design (DDD) structure.  
It allows managing books and members, including borrowing and returning books.

## 1. Setup
1. Clone the repo:
git clone <your-repo-url>
cd <your-repo-folder>

2. Install dependencies:
pip install -r requirements.txt

## 2. Running the Server:
1. on localhost --> uvicorn App.main:app --reload
2. using docker --> sudo docker-compose up --build

## 3. Using the API Endpoints:
Books
- Add a book: POST /books
- List all books: GET /books
- Get book by ID: GET /books/{book_id}
- Update book: PUT /books/{book_id}
- Delete book: DELETE /books/{book_id}
- Borrow a book: POST /books/{book_id}/borrow
- Return a book: POST /books/{book_id}/return

Members
- Add a member: POST /members
- List all members: GET /members
- Get member by ID: GET /members/{member_id}
- Update member: PUT /members/{member_id}
- Delete member: DELETE /members/{member_id}

## 4. Testing:
Currently, manual testing can be done via Swagger UI.
