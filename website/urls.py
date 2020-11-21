
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('seeds/', views.seeds,name='seeds'),
    path('contact/', views.contact,name='contact'),
    path('create_order/', views.CreateOrder,name='create_order'),
]
