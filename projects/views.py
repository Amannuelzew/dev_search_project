from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from datetime import date
from django.urls import reverse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from .forms import ProfileForm
from .models import Profiles
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
     if user :
        login(request,user)
        return redirect("index")
     else:
        messages.error(request,"does not match")

  return render(request,"projects/login.html")

def logout_page(request):
   logout(request)
   return redirect("login")

def signup_page(request):
   if request.method=="POST":
      form=UserCreationForm(request.POST)
      if form.is_valid():
         user=form.save(commit=False)
         user.username.lower()
         user.save()
         messages.success(request,"account created")
         login(request,user)
         return redirect("index")
      else:
         messages.success(request,"error")
   form=UserCreationForm()
   return render(request,"projects/signup.html",{"forms":form})
   

class ProfileView(FormView):
   template_name="projects/profile.html"
   form_class=ProfileForm
   success_url="/"
   redirect_authenticated_user=True

   def form_valid(self, form):
      user=form.save(commit=False)
      user.name.lower()
      user.save()
      return super().form_valid(form)

@login_required(login_url="login")
def index(request):
    developers=Profiles.objects.all()
    if request.GET.get("search_query"):
        query=request.GET.get("search_query")
        dev=[x for x in developers if query.lower() in  x["username"].lower()]
      
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