from fastapi import FastAPI
from App.presentation import books, members  # your route files

app = FastAPI(title="Library Management System")

# Include routers
app.include_router(books.router, prefix="/books", tags=["Books"])
app.include_router(members.router, prefix="/members", tags=["Members"])
