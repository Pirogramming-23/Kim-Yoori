##reviews/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('new/', views.review_create, name='review_create'),
    path('<int:pk>/', views.review_detail, name='review_detail'),
    path('<int:pk>/edit/', views.review_edit, name='review_edit'),
    path('<int:pk>/delete/', views.review_delete, name='review_delete'),
]