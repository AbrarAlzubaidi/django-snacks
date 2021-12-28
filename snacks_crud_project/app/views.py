from django.shortcuts import render
from django.db import models
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Snacks
from django.urls import reverse_lazy
# list view
class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snacks

# detail view
class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snacks
    context_object_name = 'snack'

# create view
class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model = Snacks
    fields = ['title', 'purchaser', 'description']


# update view
class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model = Snacks
    fields = ['title', 'purchaser', 'description']

# delete view
class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snacks
    success_url = reverse_lazy('snacks_list')
