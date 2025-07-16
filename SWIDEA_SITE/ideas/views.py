from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Idea, IdeaStar

# 아이디어 리스트 출력
def idea_list(request):
    #정렬 기준 받기
    sort = request.GET.get('sort', 'latest')

    if sort == 'name':
        ideas = Idea.objects.all().order_by('title')
    elif sort == 'stars':
        ideas = Idea.objects.annotate(star_count=Count('ideastar')).order_by('-star_count')
    elif sort == 'oldest':
        ideas = Idea.objects.all().order_by('created_at')
    else:
        ideas = Idea.objects.all().order_by('-created_at')
    
    #찜한 상태를 딕셔너리 형태로 전달
    star_dict = {}
    if request.user.is_authenticated:
        starred = IdeaStar.objects.filter(user=request.user).values_list('idea_id', flat=True)
        star_dict = {idea.id: True for idea in ideas if idea.id in starred}

    return render(request, 'ideas/idea_list.html', {
        'ideas':ideas,
        'star_dict':star_dict
    })

#로그인하지 않은 사용자가 이 view에 접근하면 자동으로 로그인 페이지로 이동하게 만드는 문법
@login_required
def toggle_star(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    user = request.user

    existing_star = IdeaStar.objects.filter(user=user, idea=idea).first()
    if existing_star:
        existing_star.delete()
    else:
        IdeaStar.objects.create(user=user, idea=idea)
    #다시 아이디어 리스트로 이동
    return redirect('ideas:idea_list')
