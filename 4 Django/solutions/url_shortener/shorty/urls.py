from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('shorten', views.shorten, name = 'shorten'),
    path('list', views.list_urls, name = 'list'),
    path('random', views.random_url, name = 'random'),
    path('<slug:url_hash>', views.redirector, name = 'redirect'),
]