from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('like/<int:post_id>/', views.toggle_like, name='toggle_like'),
]
