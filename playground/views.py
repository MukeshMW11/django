from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def calculate():
    x=1
    y=2
    result = x + y
    return HttpResponse(f'The result is {result}')

def say_hello(request):
    calculate()
    return render(request,'index.html',{'name':'Josh Murgrate'})