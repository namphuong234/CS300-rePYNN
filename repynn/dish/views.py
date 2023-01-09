from django.shortcuts import render
from .models import Dish, Category
from django.http import Http404


def dish_menu(request):
    dishes = Dish.objects.all()
    categories = Category.objects.all()
    return render(request, 'dish_menu.html', {
        'dishes': dishes,
        'categories': categories
    })


def dish_detail(request, pid):
    try:
        dish_detail = Dish.objects.get(id=pid)
    except Dish.DoesNotExist:
        raise Http404("Dish is not found.")
    return render(request, 'dish_detail.html', {'dish': dish_detail})

