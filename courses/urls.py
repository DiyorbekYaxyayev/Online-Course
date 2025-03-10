from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('courses/', views.courses, name='courses'),
    path('course-detail/', views.course_detail, name='course-detail'),
]