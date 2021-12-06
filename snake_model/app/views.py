from django.shortcuts import render
from django.db import models
from django.views.generic import ListView, DetailView
from .models import Snakes
# Create your views here.

class SnacksListView(ListView):
    template_name = 'snack_list.html'
    model = Snakes

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snakes