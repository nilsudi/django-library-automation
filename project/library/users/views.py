from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Books
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import BookForm


@csrf_exempt
def addBook(request):
    submitted = False
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/new_book?submitted=True')
    else:
        form = BookForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'new-book.html', {'form':form, 'submitted':submitted})

def updateBook(request, bookId):
    submitted = False
    book = Books.objects.get(bookId = bookId)
    if request.method == 'POST':
        form = BookForm(request.POST or None, request.FILES,  instance=book)
        if form.is_valid():
            form.save()
            submitted = True
        else:
            print(form.errors)
    else:
        form = BookForm(instance = book)
    return render(request, 'update_book.html', {'book':book, 'form': form, 'submitted': submitted})

def books(request):
    if request.method == 'POST':
        book = request.POST['delete']
        Books.objects.get(pk=bookId).delete()
    bookList = Books.objects.all().values()
    print(bookList)
    schema = loader.get_template('books.html')
    data = {
     'bookList': bookList
     }
    return HttpResponse(schema.render(data, request))

def bookDetails(request, bookId):
    book = {'book': Books.objects.get(bookId = bookId)}
    schema = loader.get_template('book_details.html')
    return HttpResponse(schema.render(book, request))

def deleteBook(request, bookId):
    book = Books.objects.get(bookId = bookId)
    book.delete()
    return render(request,'_deleteinfo.html')