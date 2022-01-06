from django.shortcuts import render

# Create your views here.
def home(request):
    """Index page"""

    return render(request, 'main/index.html')