from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Idea, IdeaStar
from django.views.decorators.http import require_POST
from .forms import IdeaForm

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

#관심도 조절 
@require_POST
@login_required
def adjust_interest(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    action = request.POST.get('action')

    if action == 'increase':
        idea.interest += 1
    elif action == 'decrease' and idea.interest > 0:
        idea.interest -= 1
    
    idea.save()
    return redirect('ideas:idea_list')

#아이디어 등록
@login_required
def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect('ideas:idea_list')
    else:
        form = IdeaForm()
    
    return render(request, 'ideas/idea_form.html', {'form':form})

def idea_detail(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    
    is_starred = False
    if request.user.is_authenticated:
        is_starred = IdeaStar.objects.filter(user=request.user, idea=idea).exists()
    
    return render(request, 'ideas/idea_detail.html', {
        'idea':idea,
        'is_starred': is_starred
    })

#삭제
@login_required
def idea_delete(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)

    if request.method == 'POST':
        idea.delete()
        return redirect('ideas:idea_list')
    
    return render(request, 'ideas/idea_confirm_delete.html', {'idea':idea})

#수정
@login_required
def idea_update(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)

    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('ideas:idea_detail', idea.id)
    else:
        form = IdeaForm(instance=idea)

    return render(request, 'ideas/idea_form.html', {'form' : form})