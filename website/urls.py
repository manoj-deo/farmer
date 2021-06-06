
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name=''),
    path('home', views.home, name='home'),
    path('seeds/', views.seeds,name='seeds'),
    path('contact/', views.contact,name='contact'),
    path('create_order/', views.CreateOrder,name='create_order'),
]
