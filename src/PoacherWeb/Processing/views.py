from django.shortcuts import render
from django.http import HttpResponse
from .models import PoacherImage
from .forms import *
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from Model import firstModel

# Create your views here.
def index(request):
    PoacherF = PoacherForm()
    return render(request, 'Processing.html', {'form': PoacherF})

def Process(request):
    print(request.POST)
    return HttpResponse('In Process It')

class Home(TemplateView):
    template_name = 'Processing.html'

def upload(request):
    context={}
    if(request.method=='POST'):
        uploaded_file = request.FILES['image']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs=FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(name)
        probability = firstModel.determineProbability(uploaded_file.name)
        print(probability)
    return render(request,'Processing.html')

