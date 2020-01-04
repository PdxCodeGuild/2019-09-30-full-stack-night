from django.contrib import admin

from catalog.models import Book, BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'id')
        }),
        ('availability', {
            'fields': ('status' , 'due_back', 'borrower')

        }),

    )