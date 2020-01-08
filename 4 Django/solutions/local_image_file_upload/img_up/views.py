from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import ImageDocument

def index(request):
    
    return render(request, 'index.html', {"images": ImageDocument.objects.all()})

def upload(request):
    ImageDocument.objects.create(
        image_file = request.FILES['image_file']
    )

    return redirect('home')