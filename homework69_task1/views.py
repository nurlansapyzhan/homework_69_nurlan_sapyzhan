import json

from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.
def add(request):
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
        result = a + b
    return JsonResponse({'answer': result})


def subtract(request):
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
        result = a - b
    return JsonResponse({'answer': result})


def multiply(request):
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
        result = a * b
    return JsonResponse({'answer': result})


def divide(request):
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
        if b == 0:
            return HttpResponseBadRequest('Fatal Error. Division by zero')
        result = a / b
    return JsonResponse({'answer': result})


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')
