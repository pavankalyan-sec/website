from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def menu(request):
    return render(request, 'menu.html')
def contactus(request):
    return render(request, 'contactus.html')
def administration(request):
    return render(request, 'administration.html')
