from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 개발툴 모델
class DevTool(models.Model):
    name = models.CharField(max_length=100) #개발툴 이름
    kind = models.CharField(max_length=100) #개발툴 종류
    content = models.TextField() #개발툴 설명

    def __str__(self):
        return self.name
   
class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

#아이디어 게시물 모델
class Idea(models.Model):
    title = models.CharField(max_length=200) #아이디어 제목
    image = models.ImageField(upload_to='idea_images/') #썸네일 이미지 저장 경로
    content = models.TextField() #아이디어 설명
    interest = models.PositiveIntegerField(default=0) #관심도 숫자

    #외래키: 어떤 개발툴을 사용하는 아이디어인지 연결
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE, related_name='ideas')
    #작성시간, 수정시간
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)

#찜 기능 모델
class IdeaStar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'idea')

