from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'shapelinterior/index.html', {})


def about(request):
    return render(request, 'shapelinterior/about.html', {})


def blog(request):
    return render(request, 'shapelinterior/blog.html', {})


def gallery(request):
    return render(request, 'shapelinterior/gallery.html', {})


def service(request):
    return render(request, 'shapelinterior/service.html', {})
