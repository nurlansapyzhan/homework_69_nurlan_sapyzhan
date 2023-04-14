import json

from django.http import HttpResponseBadRequest, JsonResponse


# Create your views here.
def add(request):
    if request.body:
        content = json.loads(request.body)
        a = content.get('A')
        b = content.get('B')
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
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            return HttpResponseBadRequest('A or B is not a number')
    if b == 0:
        return HttpResponseBadRequest('Fatal error. Division by zero')
    else:
        result = a / b
        return JsonResponse({'answer': result})
