from django.shortcuts import render
from .models import Message

def home(request):
    #messages = Message.objects.all()
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

def send_message(request):
    sender = request.POST.get('sender')
    message = request.POST.get('message')
    Message.objects.create(sender=sender, message=message)
    return redirect('home')
