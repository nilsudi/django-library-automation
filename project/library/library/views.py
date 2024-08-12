from django.shortcuts import render
from users.models import Books,Users

def home(request):
 books = Books.objects.count()
 users = Users.objects.count()

 data={
    'bookcount'  : books,
    'users' :  users,
 }
 return render(request,'index.html',{'data':data})

