from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('blog', views.blog, name="blog"),
    path('gallery', views.gallery, name="gallery"),
    path('service', views.service, name="service")

]
