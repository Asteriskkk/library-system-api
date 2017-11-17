from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Book,Author,BookInstance
from django.shortcuts import get_object_or_404


class BookListView(LoginRequiredMixin,ListView):
    model = Book
    paginate_by = 5


class BookDetailView(LoginRequiredMixin,DetailView):
	model = Book



class AuthorListView(LoginRequiredMixin,ListView):
    model = Author
    paginate_by = 5



class AuthorDetailView(LoginRequiredMixin,DetailView):
	model=Author
    

class LoanedBooksByUserListView(LoginRequiredMixin,ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

        
 






