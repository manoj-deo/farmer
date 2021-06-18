
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('login/', views.login, name='login'),
    path('seeds/', views.seeds,name='seeds'),
    path('contact/', views.contact,name='contact'),
    #path('create_order/', views.CreateOrder,name='create_order'),
    path('create_order/<str:pk>/', views.CreateOrder,name='create_order'),
]
