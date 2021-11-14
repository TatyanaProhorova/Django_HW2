
from django.http import HttpResponse
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

# def omlet(request, servings):
# result = {
#     "omlet": {
#         key: (value * servings) for key, value in DATA['omlet'].items()
#     }
# }
# return result
# quantity = request.GET.get('quantity', 1)
# print(list(DATA['omlet'].items()))
recipe = DATA

def omlet(servings):
    result = {
            key: (value * servings) for key, value in list(DATA["recipe"].items())
           for "recipe" in DATA.keys()
        }
    }
    return result

print(omlet(4))