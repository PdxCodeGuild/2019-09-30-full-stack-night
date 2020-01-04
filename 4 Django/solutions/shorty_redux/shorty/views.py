from django.shortcuts import render, redirect

from .models import Url

def shorten_url(request):
    if request.method == 'POST':
        url = request.POST['url']
        if not Url.objects.filter(url = url).exists():
            new_url = Url.objects.create(
                url = url,
                url_hash = hash(url)
            )
            context = {
                "shortened_url": new_url
            }
            return render(request, 'index.html', context)
        else:
            context = {
                "shortened_url": Url.objects.get(url = url)
            }
            return render(request, 'index.html', context)


    return render(request, 'index.html')

def shortened_redirect(request, url_hash):
    url = Url.objects.get(url_hash = url_hash)
    return redirect(url.url)
