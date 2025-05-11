from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Home:Hello World, you are at learning phase from Chai aur code")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("About:Hello World, you are at learning phase from Chai aur code")
    return render(request, 'website/about.html')


def contact(request):
    # return HttpResponse("Contact:Hello World, you are at learning phase from Chai aur code")
    return render(request, 'website/contact.html')

def ahsan(request):
    # return HttpResponse("Ahsan Ka Page")
    return render(request, 'website/ahsan.html')

