from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    peoples=[
        { "name":"rahul", "age":24,},
         {"name":"suhani","age":21},
         {"name":"suhani","age":21},
         {"name":"suhani","age":21},
         {"name":"suhani","age":21},
         {"name":"suhani","age":21},
         {"name":"suhani","age":21}
        
    ]
    return HttpResponse("hello")
