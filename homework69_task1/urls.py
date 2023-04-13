from django.urls import path

from homework69_task1.views import add, subtract, multiply, divide

urlpatterns = [
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide')
]
