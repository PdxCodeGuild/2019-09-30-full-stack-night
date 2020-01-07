from django.urls import path

from todo_app.models import Todo

from . import views

urlpatterns = [
    path('', views.TodoList.as_view()),
    path('<int:pk>/', views.TodoDetail.as_view()),
]