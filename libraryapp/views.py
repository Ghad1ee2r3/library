from django.shortcuts import render ,  redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Book ,Memberships
from datetime import datetime
import time
from django.utils import timezone
from .forms import BookForm ,MembershipsForm , SignupForm, SigninForm
from django.db.models import Q
from django.db.models.functions import Coalesce
from django.core.mail import send_mail

#def send(request):
#    send_mail('hello','you are member know','apps02977@gmail.com',['ghadeeraskaralanazi@gmail.com'],fail_silently=False)
#    return render (request, 'send.html')

# Create your views here.



def profile(request):
    v=request.user.username
    memberships=Memberships.objects.filter(user=v)
    d=datetime.now()
    #c="2020-09-09"
    #a=timezone.now
    current=Memberships.objects.filter(datereturn=d)

    context = {
        "current": current,
        "memberships": memberships
    }
    return render(request, 'profile.html', context)
    #return render(request, 'profile.html')

def notallow(request):
    return render(request, 'notallow.html')


def signout(request):
    logout(request)
    return redirect("signin")


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            #user.is_active = False
            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("book-list")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)



def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect('book-list')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)


def book_create(request):
    #book_obj = Book.objects.get(id=book_id)
    #if request.user  == request.user.is_staff  or    request.user.is_anonymous   : # admin #or request.user.is_staff normal user
    #    return redirect('notallow')
    #if request.user.is_anonymous:
        #return redirect('signin')
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.librarian = request.user
            book.save()
            return redirect('book-list')
    context = {
        "form":form,
    }
    return render(request, 'create_book.html', context)

def membership_create(request):
    #book_obj = Book.objects.get(id=book_id)
    #if request.user  == request.user.is_staff  or    request.user.is_anonymous   : # admin #or request.user.is_staff normal user
    #    return redirect('notallow')
    #if request.user.is_anonymous:
        #return redirect('signin')
    form = MembershipsForm()
    if request.method == "POST":
        form = MembershipsForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            #book.librarian = request.user
            book.save()
            #send_mail('hello','you are member know','apps02977@gmail.com',['ghadeeraskaralanazi@gmail.com'],fail_silently=False)
            return redirect('book-list')
    context = {
        "form":form,
    }
    return render(request, 'create_member.html', context)


def search_list(request ):
    #query= request.GET['search_query']
    #obj_query=Book.objects.filter(Q(name__contains="book")|Q(isbn=int(""))|Q(genre=""))
    #query=Book.objects.filter(Q(name__contains=query)|Q(isbn=int(query))|Q(genre=query))
    query = Book.objects.filter(name="book")
    context = {
        #"Books": books,
        #"Bookss":Bookss,
        "query":query
    }
    return render(request, 'book_list2.html', context)



def book_list(request):
    Bookss = Book.objects.all()
    books = Book.objects.filter(available="True")
    #from django.db.models import Q
    #query=Book.objects.filter(Q(name__contains="book")|Q(isbn=int("1111"))|Q(genre="education"))
    context = {
        "Books": books,
        "Bookss":Bookss,
        #"query":query
    }
    return render(request, 'book_list.html', context)





def book_detail(request, book_id):
    books = Book.objects.get(id=book_id)
    field_name = 'name'
    obj = Book.objects.first()
    field_object = Book._meta.get_field(field_name)
    field_value = getattr(obj, field_object.attname)
    #value =field_object.book.name
    #example = MyModel.objects.get(pk=1)
    v=books.name
    #classroom.order_by('name')   namebook__contains=v
    #students=Student.objects.filter(classroom=classroom)#.extra(select={"name":"LOWER(NAME)"},order_by="name") memberships=Memberships.objects.filter(book=books) #return first obj membership
    memberships=Memberships.objects.filter(namebook=v)
    context = {
        "book": books,
        "memberships": memberships
    }
    return render(request, 'book_detail.html', context)


def log_create(request, book_id):
    book = Book.objects.get(id=book_id)
    #if not request.user == classroom.teacher:
    #    messages.success(request,"sign in as teacher")
    #    return redirect('signin')
    form = MembershipsForm()
    if request.method == "POST":
        form = MembershipsForm(request.POST)
        if form.is_valid():
            membership = form.save(commit=False)
            membership.book = book
            membership.save()
            return redirect('list-detail', book_id)
    context = {
        "form":form,
        "book": book,
    }
    return render(request, 'log_create.html', context)


#def book_update()
def book_update(request, book_id):
    book = Book.objects.get(id=book_id)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Edited!")
            return redirect('book-list')
        print (form.errors)
    context = {
    "form": form,
    "book": book,
    }
    return render(request, 'update_book.html', context)


#def profile(request):
