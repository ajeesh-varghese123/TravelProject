from django.http import HttpResponse
from django.shortcuts import render
from . models import Places
from . models import Clients

# Create your views here.
def demo(request):
    obj=Places.objects.all()
    obj1=Clients.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})










# def registration(request):
#     return render(request,"registration.html")
#
# def content(request):
#     return HttpResponse("Hii inmakes")

#def operation(request):
   # x=int(request.GET['num1'])
   # y=int(request.GET['num2'])
   # add=x+y
   # sub=x-y
   # mul=x*y
   # div=x/y
   # return render(request,"log.html",{'addit':add,'subtrat':sub,'multiplicat':mul,'divis':div})