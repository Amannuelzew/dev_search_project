from django.shortcuts import render
from datetime import date
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
     "tags":["c#","c++","c","GraphQL"]}
]
def index(request):
    if request.GET.get("search_query"):
        query=request.GET.get("search_query")
        dev=[x for x in developers if x["username"].lower()==query]
        print(len(dev) )
        context={"developers":dev}
        return render(request,"projects/index.html",context)
    
    context={"developers":developers}
    return render(request,"projects/index.html",context)