from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('todos/', include('todo_app.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
]
