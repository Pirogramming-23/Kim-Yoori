from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    user = User.objects.get(username='yoyoo_rii')
    user_posts = Post.objects.filter(author=user).order_by('-created_at')
    post_count = user_posts.count()

    return render(request, 'posts/index.html', {
        'user_profile': user,
        'posts': user_posts,
        'post_count': post_count,
    })

def toggle_like(request, post_id):
    if request.method == 'POST' and request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        if user in post.likes.all():
            post.likes.remove(user)
            liked = False
        else:
            post.likes.add(user)
            liked = True
        
        return JsonResponse({
            'liked': liked,
            'likes_count': post.likes.count(),
        })
    
    return JsonResponse({'error': '로그인이 필요합니다.'}, status=401)

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_detail.html', {
        'post': post,
        'user': request.user, 
    })

import json
@csrf_exempt
def add_comment(request, post_id):
    if request.method == 'POST' and request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        try:
            data = json.loads(request.body)
            content = data.get('content') 

            if content:
                post.comments.create(author=request.user, content=content)
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': '내용이 비어있습니다.'})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': '로그인이 필요합니다.'}, status=401)

@require_POST
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.user == comment.author:
        comment.delete()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': '권한이 없습니다.'}, status=403)
