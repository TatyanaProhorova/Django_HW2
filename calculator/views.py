from django.shortcuts import render
# from django.http import HttpResponse
from decimal import Decimal

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def find_dish(request, item):
    if request.GET.get("servings") is None:
        servings = 1
    else:
        servings = int(request.GET.get("servings"))

    context = {
        "recipe": {
            key: round(value * servings, 1) for key, value in DATA[str(item)].items()
        }
    }
    result = render(request, 'calculator/index.html', context)
    return result


#для запуска
#python recipes/manage.py runserver
#для запроса
#/omlet/?servings=5