from django.urls import path

from . import views

urlpatterns = [
    path('', views.todo_list, name = 'list'),
    path('details/<int:id>', views.details, name = 'details'),
    path('add/', views.add_todo, name = 'add'),
    path('remove/<int:id>', views.remove_todo, name = 'remove'),
    path('mark/<int:id>', views.mark_done, name = 'mark'),
    path('update/<int:id>', views.update, name = 'update'),
]
