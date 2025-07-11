from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
# review_list 페이지
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/review_list.html', {'reviews':reviews})

# review_create 페이지
def review_create(request):
    if request.method == 'POST' :
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form' : form})