from django.shortcuts import render

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


def omlet(request):
    if request.GET.get("servings") is None:
        servings = 1
    else:
        servings = int(request.GET.get("servings"))
    context = {
        "omlet": {
            key: (value * servings) for key, value in DATA['omlet'].items()
        }
    }

    result = render(request, 'calculator/index.html', context)
    return result


#для запуска
#python recipes/manage.py runserver
#/omlet/5/
#/omlet/?servings=5