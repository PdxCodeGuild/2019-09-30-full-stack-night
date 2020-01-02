from django.urls import path

from . import views

urlpatterns = [
    path('', views.shorten_url, name = 'shorten'),
    path('redirect/<slug:url_hash>', views.shortened_redirect, name = 'shortened_redirect'),
]