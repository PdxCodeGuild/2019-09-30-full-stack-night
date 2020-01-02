from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Url
from django.contrib import messages
from ipware import get_client_ip
import json
from hashlib import md5
from random import choice
from django.core.paginator import Paginator


def index(request):
    return render(request, 'pages/index.html')


def list_urls(request):
    url_list = Url.objects.all().order_by('-date_added')

    page = request.GET.get('page', 1)
    paginator = Paginator(url_list, 5)
    url_list = paginator.page(page)

    context = {
        'url_list': url_list,
    }

    return render(request, 'shorty/list.html', context)


def random_url(request):
    rand_url = choice(Url.objects.all()).url

    return redirect(rand_url)


def random_string(string, string_length = 7):
     return ''.join(choice(string) for i in range(string_length))


def shorten(request):
    if request.method == 'POST':
        user_url = request.POST['user_url']

        if Url.objects.all().filter(url = user_url).exists():
            user_url = Url.objects.get(url = user_url)
            user_url.repeat_addition = user_url.repeat_addition + 1
            user_url.save()
            messages.add_message(request, messages.INFO, user_url.url_hash)
            return redirect('index')
        else:
            hashed_url = md5(user_url.encode())
            url_hash = random_string(hashed_url.hexdigest())
            new_url = Url.objects.create(url = user_url, url_hash = url_hash)

            messages.add_message(request, messages.INFO, url_hash)

            return redirect('index')


def redirector(request, url_hash):
    url_entry = Url.objects.get(url_hash = url_hash)
    print(url_entry)
    ip, is_routable = get_client_ip(request)

    if ip is None:
        print(f'Unable to get the client\'s IP address')
    else:
        url_entry.last_ip = ip

    url_entry.clicks = url_entry.clicks + 1
    url_entry.save()

    return redirect(url_entry.url)