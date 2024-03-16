from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'school/home.html')

def contact(request):
    return render(request, 'school/contact.html')

def about(request):
    return render(request, 'school/about.html')