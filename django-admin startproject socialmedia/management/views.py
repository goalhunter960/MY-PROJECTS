from django.shortcuts import render

def home(request):
    return render(request, 'management/home.html')

def services(request):
    return render(request, 'management/services.html')

def pricing(request):
    return render(request, 'management/pricing.html')

def about_us(request):
    return render(request, 'management/about_us.html')

def contact(request):
    return render(request, 'management/contact.html')
