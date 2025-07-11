from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect

# Create your views here.
# review_list 페이지
def review_list(request):
    reviews = Review.objects.all().order_by('-release_year')
    return render(request, 'reviews/review_list.html', {'reviews':reviews})

# review_create 페이지
def review_create(request):
    if request.method == 'POST' :
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            form.save_m2m()
            return redirect('review_detail', pk=review.pk)
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form' : form})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)

    hours = review.running_time // 60
    minutes = review.running_time % 60
    formatted_runtime = f"{hours}시간 {minutes}분"

    return render(request, 'reviews/review_detail.html', {
        'review' : review,
        'formatted_runtime' : formatted_runtime,
    })

def review_edit(request, pk):
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', pk=review.pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'reviews/review_form.html', {'form':form})

def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('review_list')
    return render(request, 'reviews/review_confirm_delete.html', {'review' : review})