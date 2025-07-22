from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('like/<int:post_id>/', views.toggle_like, name='toggle_like'),
    path('<int:post_id>/detail/', views.post_detail, name='post_detail'),
    path('<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('search/', views.search_posts, name='search_posts'),
]