from django.db import models

# Create your models here.


class Authors(models.Model):
    authorId = models.IntegerField(unique = True)
    author_name = models.CharField(max_length =250)
    birth_year = models.IntegerField()
    def __str__(self):
        return f"{self.author_name}"




class Books(models.Model):
    bookId = models.IntegerField(unique = True)
    book_name = models.CharField(max_length = 200)
    author_name = models.CharField(max_length = 250)
    publisher = models.CharField(max_length = 100)
    book_image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(Authors,null=True, blank=True, on_delete = models.CASCADE , related_name='author')
    def __str__(self):
        return f"{self.book_name}"



class Users(models.Model):
    userno = models.IntegerField(unique = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    field = models.CharField(max_length = 50)
    email = models.CharField(max_length = 150)
    books = models.ManyToManyField(Books, related_name = 'favorites', blank = True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

