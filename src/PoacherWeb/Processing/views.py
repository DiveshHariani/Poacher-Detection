from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PoacherImage
from .forms import *
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

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
        ## Lazy Loading
        from Model import firstModel


        uploaded_file = request.FILES['image']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs=FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        print(name)
        print(uploaded_file)
        context['url'] = fs.url(name)
        [probability, output_path] = firstModel.determineProbability(uploaded_file.name)
        print('#################', output_path)

        context = {
            'url': fs.url(name),
            'output_path': '/media/' + output_path,
            'probability': int(probability),
            'bool': True if int(probability) > 40 else False
        }

        print('--------------', context['probability'], type(context['probability']), context['bool'], context['url'], context['output_path'])
        return render(request, 'Result.html',context)

    return render(request,'Processing.html')

def result(request):
    return render(request,'Result.html')

def videoUpload(request):
    return render(request, 'videoUpload.html')

def videoProcess(request):
    if request.method == 'POST':
        from Model.firstModel import determineProbabilityFromVideo 
        print('////////////////////////////////////////////////')
        uploaded_video = request.FILES['image']
        print(uploaded_video.name)
        print(uploaded_video.size)
        fs=FileSystemStorage()
        name = fs.save(uploaded_video.name,uploaded_video)
        print(name)
        print(request.FILES)

        # output_path = determineProbabilityFromVideo(name)
        context = {
            'output_path': '/media/output-Animal.avi',
            'video': True
        }
        return render(request, 'Result.html', context)
    return redirect('Processing/')