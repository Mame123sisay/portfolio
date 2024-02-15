from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import contactMessage
# Create your views here.
def main(request):
    return render( request,"index.html")
def contact_view(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contactMessage.objects.create(name=name,email=email,subject=subject,message=message)
        return redirect('contact')
    
    return render(request,'contact.html')