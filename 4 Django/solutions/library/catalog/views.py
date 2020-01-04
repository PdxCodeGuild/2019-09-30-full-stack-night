from django.shortcuts import render
from catalog.models import BookInstance
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required

@login_required
def checkout(request, book_id):

    book_to_checkout = BookInstance.objects.get(id=book_id)

    book_to_checkout.borrower = request.user
    book_to_checkout.status = 'o'
    book_to_checkout.due_back = datetime.now() + timedelta(weeks=2)

    book_to_checkout.save()

    return redirect('list_books')

@login_required
def checkin(request, book_id):
    book_to_checkin = BookInstance.objects.get(id=book_id)

    book_to_checkin.borrower = None
    book_to_checkin.status = 'a'
    book_to_checkin.due_back = None

    book_to_checkin.save()

    return redirect('dashboard')


@login_required
def list_books(request):
    all_books = BookInstance.objects.all()
    context = {
        'books' : all_books,
    }
    return render( request, 'catalog/list_books.html', context)


@login_required
def reserved(request, book_id):

    book_to_reserved = BookInstance.objects.get(id=book_id)
    book_to_reserved.borrower = request.user
    book_to_reserved.status = 'r'
    

    book_to_reserved.save()

    return redirect('list_books')
