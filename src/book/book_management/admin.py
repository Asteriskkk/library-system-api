from django.contrib import admin
from .models import Book,BookInstance,Author,Genre
admin.site.register(Book)
admin.site.register(BookInstance)

admin.site.register(Genre)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

admin.site.register(Author, AuthorAdmin)