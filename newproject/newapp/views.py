from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def news(request):
    return render(request,'news.html')
def elements(request):
    return render(request,'elements.html')
def destinations(request):
    return render(request,'destinations.html')