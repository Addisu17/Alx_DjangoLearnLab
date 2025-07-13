from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Shown in the list view
    search_fields = ('title', 'author')                     # Search bar
    list_filter = ('publication_year',)                     # Sidebar filter
