from django.urls import path
from . import views

urlpatterns = [
 path('new_book/', views.addBook),
 path('books', views.books),
 path('book_details/<int:bookId>', views.bookDetails),
 path('update/<int:bookId>', views.updateBook),
 path('delete/<int:bookId>', views.deleteBook)
]