from django.shortcuts import render, get_object_or_404
from .models import Dish
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone


# function based views
#
# def home(request):
#     dania = Dish.objects.order_by('-added')[:8]
#     return render(request, 'blog/home.html', {'dania': dania})


# def detail(request, dish_id):
#     detail_dish = get_object_or_404(Dish, pk=dish_id)
#     return render(request, 'blog/detail.html', {'dish': detail_dish})


# Class Based Views
class HomePageView(ListView):
    model = Dish
    template_name = 'blog/home.html'
    paginate_by = 8
    ordering = 'added'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        #context['dania'] = Dish.objects.order_by('-added')[:8]
        return context


class DetailDishView(DetailView):
    model = Dish
    template_name = 'blog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
