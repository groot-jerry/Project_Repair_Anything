from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_technician:
                login(request, user)
                return redirect('technician')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


from django.contrib.auth.decorators import login_required
from .forms import TechnicianProfileForm
from .models import TechnicianProfile


@login_required
def update_profile(request):
    try:
        technician_profile = request.user.technicianprofile
    except TechnicianProfile.DoesNotExist:
        technician_profile = TechnicianProfile(user=request.user)
        technician_profile.save()

    if request.method == 'POST':
        form = TechnicianProfileForm(request.POST, instance=technician_profile)
        if form.is_valid():
            form.save()
            return redirect('technician')  # Redirect to the technician's profile page
    else:
        form = TechnicianProfileForm(instance=technician_profile)
    return render(request, 'update_profile.html', {'form': form})


def admin(request):
    return render(request, 'admin.html')


def customer(request):
    return render(request, 'customer.html')


def technician(request):
    return render(request, 'technician.html')


def technician_list(request):
    return render(request, 'technician_list.html')


# views.py

from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse


def logout_view(request):
    logout(request)
    return redirect('login_view')  # Redirect to the login page after logging out


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_technician_profile(sender, instance, created, **kwargs):
    if created and instance.is_technician:
        TechnicianProfile.objects.create(user=instance)


from django.shortcuts import render
from .models import TechnicianProfile
from django.contrib.auth.decorators import login_required


@login_required
def view_technician_profile(request):
    try:
        technician_profile = request.user.technicianprofile
    except TechnicianProfile.DoesNotExist:
        technician_profile = None

    return render(request, 'technician_profile.html', {'technician_profile': technician_profile})

# from django.shortcuts import render, redirect
# from .models import TechnicianProfile
# from django.contrib.auth.decorators import login_required
# from django.urls import reverse

# @login_required
# def view_technician_profile(request):
#     try:
#         technician_profile = request.user.technicianprofile
#         if not technician_profile.is_complete():  # Check if profile is complete
#             return redirect(reverse('update_profile'))  # Redirect to profile update page
#     except TechnicianProfile.DoesNotExist:
#         return redirect(reverse('update_profile'))  # Redirect to profile update page

#     return render(request, 'technician_profile.html', {'technician_profile': technician_profile})
