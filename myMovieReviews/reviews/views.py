from django.shortcuts import render
from .models import Review

# Create your views here.
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews' : reviews})