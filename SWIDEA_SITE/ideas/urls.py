from django.urls import path
from . import views

app_name = 'ideas'

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('star/<int:idea_id>/', views.toggle_star, name='toggle_star'),
]