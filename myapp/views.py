from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import csv

def index(request):
    return render(request,"index.html")

@csrf_exempt
def register(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        upw = request.POST.get("upw")
        from .models import Data
        db = Data(name=uname,pw=upw)
        db.save()
        return render(request, "index.html",{"msg":"You Are Registered, Please Login"})
    else:
        return render(request, "index.html")

@csrf_exempt
def login(request):
    if request.method == "GET":
        uname = request.POST.get("uname")
        upw = request.POST.get("upw")
        from .models import Data
        login = Data.objects.filter(name=uname,pw=upw)
        return render(request,"show.html",{"login":login})

@csrf_exempt
def viewall(request):
    if request.method == "GET":
        from .models import Scrap
        data = Scrap.objects.all()
        return render(request,"show.html",{"data":data})
    else:
        return render(request,"show.html")

@csrf_exempt
def scrap(request):
    if request.method == "POST":
        from .models import Scrap
        dread = csv.reader(open("/home/lovey/atul/django/hi5/templates/t.csv"), delimiter=',', quotechar='"')
        for row in dread:
            scrap = Scrap()
            scrap.store_name = row[5]
            scrap.address = row[1]
            scrap.locality = row[3]
            scrap.phone = row[4]
            scrap.img_path = row[2]
            scrap.save()
        return render(request,"show.html",{"done":"Data saved in DB"})
    else:
        return render(request,"show.html")

