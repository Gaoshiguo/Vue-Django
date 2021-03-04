from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get_all_student_information/', views.get_all_student_information),
    path('get_current_detail_student/', views.get_current_detail_student),
    path('get_student_score_chart/', views.get_student_score_chart),
    path('get_student_depend_score/', views.get_student_depend_score),
    path('get_student_number/', views.get_student_number)
]
