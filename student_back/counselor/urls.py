from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get_all_school_information/', views.get_all_school_information),
]