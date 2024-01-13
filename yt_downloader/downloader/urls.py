from django.urls import path
from .views1 import index

urlpatterns = [
    path('', index, name='index'),
]
