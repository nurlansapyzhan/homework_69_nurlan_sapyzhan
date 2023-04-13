import json

from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.
def get_data(request):
    if request.body:
        content = json.loads(request.body)
        a = content.get('A')
        b = content.get('B')
        if a is None or b is None:
            return HttpResponseBadRequest('Missing A or B')
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            return HttpResponseBadRequest('A or B is not a number')
        return a, b
    else:
        return HttpResponseBadRequest('Missing Data')


def add(request):
    numbers = get_data(request)
    result = numbers[0] + numbers[1]
    return JsonResponse({'answer': result})


def subtract(request):
    numbers = get_data(request)
    result = numbers[0] - numbers[1]
    return JsonResponse({'answer': result})


def multiply(request):
    numbers = get_data(request)
    result = numbers[0] * numbers[1]
    return JsonResponse({'answer': result})


def divide(request):
    numbers = get_data(request)
    if numbers[1] == 0:
        return HttpResponseBadRequest('Fatal Error. Division by zero')
    else:
        result = numbers[0] / numbers[1]
        return JsonResponse({'answer': result})
