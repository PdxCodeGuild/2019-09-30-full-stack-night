from django.urls import path
from . import views

urlpatterns =  [
    path('checkout/<slug:book_id>', views.checkout , name = 'checkout' ),
    path('checkin/<slug:book_id>', views.checkin , name = 'checkin'),
    path('list_books' , views.list_books , name = 'list_books'),
]