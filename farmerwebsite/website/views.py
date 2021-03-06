from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
# Create your views here.
def home(request):
   return render(request, 'website/home.html')

def seeds(request):
   seeds_table =Product.objects.all()
   return render(request, 'website/seeds.html', {"content": seeds_table })

def contact(request):
   return render(request, 'website/contact.html')

def CreateOrder(request):
    form=OrderForm()
    if request.method == 'POST':
        print('PRINTING POST DATA:',request.POST)
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}
    return render(request, "website/order_form.html",context)

def contact(request):
   if request.method == 'POST':
      fname = request.POST.get('fname')
      lname = request.POST.get('lname')
      address = request.POST.get('address')
      subject = request.POST.get('subject')
      #send_mail(subject, fname, lname, ['manoj.deo91@gmail.com'], fail_silently=False)
      message1 = ('Subject here', fname, 'from@example.com', ['manoj.deo91@gmail.com'])
      message2 = ('Another Subject', lname,  'from@example.com',['manoj.deo91@gmail.com'])
      send_mass_mail((message1, message2), fail_silently=False)
   return render(request, 'website/contact.html')
