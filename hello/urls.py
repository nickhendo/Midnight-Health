from django.urls import path

from . import views

urlpatterns = [
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact, name='contact'),
    path('', views.index, name='index'),
]
