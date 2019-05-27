from django.http import HttpResponse
from django.shortcuts import render

def home_page_old(request):
    return HttpResponse('Hello World')

def home_page(request):
    context = {
        'title': 'Hello World',
        'content': 'Welcome'
    }
    return render(request, 'home_page.html', context)

def about(request):
    context = {
        'title': 'About Page',
        'content': 'Welcome to the About Page'
    }

    return render(request, 'home_page.html', context)

def contact(request):
    context = {
        'title': 'Contact Page',
        'content': 'Welcome to the Contact Page'
    }

    return render(request, 'home_page.html', context)