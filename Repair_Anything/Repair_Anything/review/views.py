from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import User
from .forms import ReviewForm

def add_review(request, technician_id):
    technician = User.objects.get(pk=technician_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.technician = technician
            review.save()
            return redirect('technician_list.html', technician_id=technician_id)
    else:
        form = ReviewForm()
    return render(request, 'add_review.html', {'form': form, 'technician': technician})

def add_review(request):
    return render(request, 'add_review.html')