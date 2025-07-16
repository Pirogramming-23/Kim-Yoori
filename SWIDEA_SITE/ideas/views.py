from django.shortcuts import render
from .models import Idea

# Create your views here.
def idea_list(request):
    ideas = Idea.objects.all().order_by('-created_at') #정렬 기준은 최신순으로 
    return render(request, 'ideas/idea_list.html', {'ideas':ideas})