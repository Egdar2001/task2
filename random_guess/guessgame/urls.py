from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),            # Home page
    path('result/', views.result, name='result'),   # Result page
]
