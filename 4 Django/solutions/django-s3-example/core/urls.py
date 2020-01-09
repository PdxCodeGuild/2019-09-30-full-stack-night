from django.urls import path

from . import views

urlpatterns = [
    path('', views.image_upload, name = 'upload'),
    path('upload/delete/<int:id>', views.delete_image, name = 'delete'),
]