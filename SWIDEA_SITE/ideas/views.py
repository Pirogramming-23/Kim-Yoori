from django.shortcuts import render
from .models import Idea

# 아이디어 리스트 출력
def idea_list(request):
    #정렬 기준 받기
    sort = request.GET.get('sort', 'latest')

    if sort == 'name':
        ideas = Idea.objects.all().order_by('title')
    elif sort == 'interest':
        ideas = Idea.objects.all().order_by('-interest')
    elif sort == 'oldest':
        ideas = Idea.objects.all().order_by('created_at')
    else:
        ideas = Idea.objects.all().order_by('-created_at')

    return render(request, 'ideas/idea_list.html', {'ideas':ideas})
