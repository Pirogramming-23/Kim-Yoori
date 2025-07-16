from django.urls import path
from . import views

app_name = 'ideas'

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('star/<int:idea_id>/', views.toggle_star, name='toggle_star'),
    path('interest/<int:idea_id>/', views.adjust_interest, name='adjust_interest'),
    path('create/', views.idea_create, name='idea_create'),
    path('<int:idea_id>/', views.idea_detail, name='idea_detail'),
    path('<int:idea_id>/delete/', views.idea_delete, name='idea_delete'),
    path('<int:idea_id>/update/', views.idea_update, name='idea_update'),
    path('devtools/', views.devtool_list, name='devtool_list'),
]