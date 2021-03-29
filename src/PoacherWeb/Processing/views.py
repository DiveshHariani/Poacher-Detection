from django.shortcuts import render
from django.http import HttpResponse
from .models import PoacherImage
from .forms import *

# Create your views here.
def index(request):
    PoacherF = PoacherForm()
    return render(request, 'Processing.html', {'form': PoacherF})

def Process(request):
    print(request.POST)
    return HttpResponse('In Process It')

