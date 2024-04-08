from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from datetime import date
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
projects=[
    {"title":"hello world","description":"hello","demo_link":"https://a.com",
     "source_link":"https://a.com","created":date(2014,4,11)}
]
developers=[
    {"username":"hello world","description":""" Lorem ipsum dolor sit, amet consectetur adipisicing elit. Cupiditate, ducimus inventore! Sunt,
                  veniam veritatis? Veritatis placeat, deleniti iure tempore veniam perspiciatis, soluta cupiditate
                  animi, exercitationem molestias nam doloremque architecto odit.""","position":"FullStack Web Designer & Developer",
     "tags":["python","react","web component","vue"]},
     {"username":"my name world","description":"name","position":"back end web",
     "tags":["c#","c++","c","GraphQL"]},
     {"username":"sol","description":"name","position":"back end web",
     "tags":["c#","c++","c","GraphQL"]},
     {"username":"don","description":"name","position":"back end web",
     "tags":["c#","c++","c","GraphQL"]},
     {"username":"joel","description":"name","position":"back end web",
     "tags":["c#","c++","c","GraphQL"]},
     {"username":"sam","description":"name","position":"back end web",
     "tags":["c#","c++","c","GraphQL"]}
]

def login_page(request):
  if request.method=="POST":
     username=request.POST.get("username")
     password=request.POST.get("password")
     user=authenticate(request,username=username,password=password)
     if user is not None:
        login(request,user)
        return redirect("index")
     else:
        print("yes")
        messages.error(request,"does not match")

  return render(request,"projects/login.html")

def logout_page(request):
   logout(request)
   return redirect("login")

def index(request):
    if request.GET.get("search_query"):
        query=request.GET.get("search_query")
        dev=[x for x in developers if query.lower() in  x["username"].lower()]
        print(len(dev) )
        context={"developers":dev}
        return render(request,"projects/index.html",context)
    
    page=request.GET.get("page")
    p=Paginator(developers,3)
    try:
       dev=p.page(page)
    except PageNotAnInteger:
       dev=p.page(1)
    except EmptyPage:
       dev=p.page(p.num_pages)
    
    print(dev)
    context={"developers":dev,"Paginator":p}
    return render(request,"projects/index.html",context)