from django.urls import path

from . import views

app_name = "blogs"




urlpatterns = [
    path('all/', views.BlogListView.as_view(), name='blogs-list'),
    path('detail/<slug:slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
]