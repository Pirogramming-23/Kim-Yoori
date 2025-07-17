from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from .models import Idea, IdeaStar, DevTool
from django.views.decorators.http import require_POST
from .forms import IdeaForm, DevToolForm
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.template.loader import render_to_string

# 아이디어 리스트 출력
def idea_list(request):
    #정렬 기준 받기
    sort = request.GET.get('sort', 'latest')
    query = request.GET.get('q', '')

    idea_queryset = Idea.objects.all()

    if query:
        idea_queryset = idea_queryset.filter(
            Q(title__icontains=query) | Q(devtool__name__icontains=query)
        )

    if sort == 'name':
        idea_queryset = idea_queryset.order_by('title')
    elif sort == 'stars':
        idea_queryset = idea_queryset.annotate(star_count=Count('ideastar')).order_by('-star_count')
    elif sort == 'oldest':
        idea_queryset = idea_queryset.all().order_by('created_at')
    else:
        idea_queryset = idea_queryset.all().order_by('-created_at')
    
    #페이지네이션
    paginator = Paginator(idea_queryset, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    #찜한 상태를 딕셔너리 형태로 전달
    star_dict = {}
    if request.user.is_authenticated:
        starred = IdeaStar.objects.filter(user=request.user).values_list('idea_id', flat=True)
        star_dict = {idea.id: True for idea in page_obj if idea.id in starred}

    return render(request, 'ideas/idea_list.html', {
        'ideas':page_obj,
        'page_obj': page_obj,
        'star_dict':star_dict,
        'query': query,
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
    return JsonResponse({'success': True, 'interest': idea.interest})

#아이디어 등록
@login_required
def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect('ideas:idea_detail', idea_id=idea.id)
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
    # 기존 정보가 폼에 채워짐 pre-fill
    else:
        form = IdeaForm(instance=idea)

    return render(request, 'ideas/idea_form.html', {'form' : form})

# 개발툴 리스트 페이지
def devtool_list(request):
    devtools = DevTool.objects.all()
    return render(request, 'ideas/devtool_list.html', {
        'devtools' : devtools
    })

@login_required
def devtool_create(request):
    if request.method == 'POST':
        form = DevToolForm(request.POST)
        if form.is_valid():
            devtool = form.save()
            return redirect('ideas:devtool_detail', tool_id=devtool.id)
    else:
        form = DevToolForm()
    return render(request, 'ideas/devtool_form.html', {'form' : form})

def devtool_detail(request, tool_id):
    devtool = get_object_or_404(DevTool, id=tool_id)
    ideas = Idea.objects.filter(devtool=devtool)
    return render(request, 'ideas/devtool_detail.html',{
        'devtool' : devtool,
        'ideas' : ideas,
    })

@login_required
def devtool_delete(request, tool_id):
    devtool = get_object_or_404(DevTool, id=tool_id)

    if request.method == 'POST':
        devtool.delete()
        return redirect('ideas:devtool_list')

    return render(request, 'ideas/devtool_confirm_delete.html', {'devtool': devtool})

@login_required
def devtool_update(request, tool_id):
    devtool = get_object_or_404(DevTool, id=tool_id)

    if request.method == 'POST':
        form = DevToolForm(request.POST, instance=devtool)
        if form.is_valid():
            form.save()
            return redirect('ideas:devtool_detail', tool_id=devtool.id)
    else: #pre-fill 구현
        form = DevToolForm(instance=devtool)

    return render(request, 'ideas/devtool_form.html', {'form': form})


def idea_by_tag(request, tag_name):
    ideas = Idea.objects.filter(tags__name=tag_name).order_by('-created_at')

    star_dict = {}
    if request.user.is_authenticated:
        starred = IdeaStar.objects.filter(user=request.user).values_list('idea_id', flat=True)
        star_dict = {idea.id: True for idea in ideas if idea.id in starred}

    return render(request, 'ideas/idea_list.html', {
        'ideas': ideas,
        'star_dict': star_dict,
        'filter_tag': tag_name,
    })

def ajax_search(request):
    query = request.GET.get('q', '')
    ideas = Idea.objects.filter(title__icontains=query).order_by('-created_at')

    html = render_to_string('ideas/partials/idea_list.html', {
        'ideas' : ideas,
        'star_dict' : {idea.id: True for idea in ideas if request.user.is_authenticated and IdeaStar.objects.filter(user=request.user, idea=idea).exists()},
        'user': request.user,
    })

    return JsonResponse({'html':html})