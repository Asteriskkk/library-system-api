from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Pet
from django.shortcuts import get_object_or_404






class PetListView(LoginRequiredMixin,ListView):
    model = Pet
    paginate_by = 5

class PetDetailView(LoginRequiredMixin,DetailView):
	model=Pet
    






