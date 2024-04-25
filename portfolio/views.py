from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/index.html')  # Assuming you have a template named 'home.html'

 #file:///P:/myportfolio/templates/portfolio/index.html