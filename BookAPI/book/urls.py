from django.urls import path
from .views import BookAPI, BooksAPI, bookAPI, booksAPI

urlpatterns = [
    path("fbv/books", booksAPI),
    path("cbv/book/<int:bid>/", BookAPI.as_view()),
]
