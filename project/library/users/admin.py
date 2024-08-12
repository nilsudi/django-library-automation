from django.contrib import admin
from .models import Users, Books, Authors

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ("userno", "first_name", "last_name", "field", "email")

class BooksAdmin(admin.ModelAdmin):
    list_display = ("bookId", "book_name", "author_name", "publisher")

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ("authorId", "author_name", "birth_year")

admin.site.register(Users, UsersAdmin)
admin.site.register(Books, BooksAdmin)
admin.site.register(Authors, AuthorsAdmin)