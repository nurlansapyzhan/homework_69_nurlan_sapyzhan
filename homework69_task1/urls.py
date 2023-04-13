from django.urls import path

from homework69_task1.views import add, get_token_view, subtract

urlpatterns = [
    path('add/', add, name='add'),
    path('token/', get_token_view, name='token'),
    path('subtract/', subtract, name='subtract'),
]
