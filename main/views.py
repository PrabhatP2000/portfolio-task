from django.shortcuts import render,HttpResponse
from .models import ContactForm

# Create your views here.

def index(request):
    return render(request, 'portfolio.html')

def contactForm(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contactform =ContactForm(NAME=name,EMAIL=email,SUBJECT=subject,MESSAGE=message)
        contactform.save()
        return render(request, 'portfolio.html')
        
    else:
        return HttpResponse("Please try again Error 404")