# review/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm

@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('technician')  # Redirect to appropriate page
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

def review_success(request):
    return render(request, "review_success.html")
