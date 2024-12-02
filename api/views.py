import heapq
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import count_common_hobbies
from .forms import UserForm, UserAuthenticationForm

from .models import User

def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

def build_max_heap(user):
    
    users = User.objects.exclude(id=user.id)
    max_heap = []
    
    for other_user in users:
        common_hobbies_count = User.count_common_hobbies(user, other_user)
        heapq.heappush(max_heap, (-common_hobbies_count, other_user))
    
    return max_heap
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Save the new user
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('home')  # Redirect to a home page or another page
    else:
        form = UserForm()
    
    return render(request, 'signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a home page or another page
    else:
        form = UserAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') 