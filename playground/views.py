from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def say_hello(request):
    #a Simple response
    # return HttpResponse("Hello World")
    return render(request, 'hello.html', {'name': 'Anis'})