from django.urls import path

from homework69_task2.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
