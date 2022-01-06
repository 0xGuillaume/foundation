from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    """Index page"""

    chars = Char.objects.all()

    context = {
        "chars": chars
    }

    return render(request, 'main/index.html', context)