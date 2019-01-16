from django.shortcuts import render, get_object_or_404

from .models import Dish


def home(request):
    dania = Dish.objects.order_by('-added')[:8]
    return render(request, 'blog/home.html', {'dania': dania})


def detail(request, dish_id):
    detail_dish = get_object_or_404(Dish, pk=dish_id)
    return render(request, 'blog/detail.html', {'dish': detail_dish})
