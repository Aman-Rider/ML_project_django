from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .utils import pipeline_model
import os
from django.conf import settings
from shutil import move

# Create your views here.
def home(request):
    return render(request, 'space/home.html')
@login_required
def faceapp(request):
    return render(request, 'space/faceapp.html')
@login_required
def gender(request):
    if request.method == 'POST':
        if request.FILES['image']:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            ext = myfile.name.split('.')[1]
            files  = '{}.{}'.format(request.user, ext)
            try:
                path = os.path.join(settings.BASE_DIR,'media\\'+files)
                os.remove(path)
            except:
                pass
            filename = fs.save(files, myfile)
            # filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            img_path = os.path.join(settings.BASE_DIR,'media\\'+files)
            pipeline_model(img_path,files,color='bgr')
            pred_path = os.path.join(settings.BASE_DIR,'upload\\predict\\'+files)
            return render(request, 'space/gender.html', {
            'uploaded_flag': True, 'file_name':files, 'predict_path' : pred_path
        })
    return render(request, 'space/gender.html')