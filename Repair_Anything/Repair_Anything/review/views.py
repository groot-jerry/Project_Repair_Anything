# review/views.py

from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def add_review(request, technician_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.technician_id = technician_id
            review.user = request.user
            review.save()
            return redirect('technician', technician_id=technician_id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form})

def review_success(request):
    return render(request= "review_success.html")