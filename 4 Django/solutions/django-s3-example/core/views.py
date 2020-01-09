from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import boto3
from decouple import config
from django.contrib.auth.decorators import login_required



from .models import Document

@login_required
def delete_image(request, id):

    image = Document.objects.get(id = id)
    
    s3 = boto3.resource(
        's3',
        aws_access_key_id = config('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key = config('AWS_SECRET_ACCESS_KEY'),
    )
    # s3 = boto3.resource('s3')
    # bucket = s3.Bucket('django-static-example')
    # print(dir(bucket.objects.all()))
    # for x in bucket.objects.all():
    #     print(x)
    # s3.delete_object(Bucket = 'django-static-example', Key = image.file.name)
    s3.Object('django-static-example', f'media/{image.file.name}').delete()
    image.delete()
    return redirect(reverse('upload'))


@login_required
def image_upload(request):
    if request.method == 'POST':
        print(request.FILES)
        image_file = request.FILES.get('image_file')
        image_type = request.POST.get('image_type')
        upload = Document(
            file=image_file,
            user = request.user
        )
        upload.save()
        image_url = upload.file.url

        return redirect(reverse('upload'))
    else:
        images = Document.objects.filter(user = request.user)
        context = {
            'images': images,
        }
        return render(request, 'core/upload.html', context)


