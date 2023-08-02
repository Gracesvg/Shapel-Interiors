from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>home page</h1>')


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def gallery(request):
    return render(request, 'gallery.html')


def service(request):
    return render(request, 'service.html')
