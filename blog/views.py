from .models import Dish
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm


# Class Based Views
class HomePageView(ListView):
    model = Dish
    template_name = 'blog/home.html'
    paginate_by = 8
    ordering = ['-added']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class DetailDishView(DetailView):
    model = Dish
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateDishView(CreateView):
    template_name = 'blog/create_dish.html'
    fields = (
        'name', 'portions', 'ingredients', 'description', 'added', 'photo0', 'photo1', 'photo2', 'rating', 'thermomix')
    model = Dish


class UpdateDishView(UpdateView):
    template_name = 'blog/create_dish.html'
    fields = (
        'name', 'portions', 'ingredients', 'description', 'added', 'photo0', 'photo1', 'photo2', 'rating', 'thermomix')
    model = Dish


class DeleteDishView(DeleteView):
    model = Dish
    success_url = reverse_lazy('home')
