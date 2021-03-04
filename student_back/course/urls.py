from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get_current_student_score/', views.get_current_student_score),
    path('get_current_student_detail_score/', views.get_current_student_detail_score),
    path('get_course_number/', views.get_course_number)
]
