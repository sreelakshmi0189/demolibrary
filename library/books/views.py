from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from books.models import Book
from books.forms import Bookform
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home.html')
@login_required
def bookdetail(request,p):
    b=Book.objects.get(id=p)
    return render(request,'book.html',{'b':b})

@login_required
def bookdelete(request,p):
    b = Book.objects.get(id=p)
    b.delete()
    return viewbook(request)

@login_required
def bookedit(request,p):
    b=Book.objects.get(id=p)
    if (request.method == "POST"):  # After submission
        form = Bookform(request.POST,request.FILES,instance=b)  # Creates form object initialized with values inside request.POST  ##instance=b kodukkunnath form fill aayt display aavan
        if form.is_valid():
            form.save()  # save the form object inside DB table
        return viewbook(request)

    form=Bookform(instance=b)
    return render(request,"editbook.html",{"form":form})

@login_required
def search(request):
    query=""
    b=None
    if(request.method=="POST"):
        query=request.POST['q']
        if(query):
            b=Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

    return render(request,'search.html',{'query':query,'b':b})
@login_required
def addbook(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        p=request.POST['p']
        f=request.FILES['f']
        i=request.FILES['i']
        b=Book.objects.create(title=t,author=a,price=p,pdf=f,cover=i)
        b.save()
        return viewbook(request)
    return render(request,'addbook.html')

@login_required
def fact(request):
    if(request.method=="POST"):
        num=int(request.POST['n'])
        f=1
        for i in range(1,num+1):
            f=f*i
        return render(request,'factorial.html',{'fact':f})
    else:
        return render(request,"factorial.html")


@login_required
def addbook1(request):
    if(request.method=="POST"): #After submission
        form=Bookform(request.POST)  #create from object initialized with values inside request.post
        if form.is_valid():
            form.save()  #save the form object inside DB table
        return viewbook(request)


    form=Bookform()  ##Empty form object with no values
    return render(request, 'addbook1.html',{'form':form})


@login_required
def viewbook(request):


    k=Book.objects.all()
    return render(request,'viewbook.html',{'b':k})

