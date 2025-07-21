from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return f"{self.author.username}'s post"

#팔로워 / 팔로우 수 
class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

