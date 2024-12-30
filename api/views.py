import heapq
import json
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .forms import UserForm, UserAuthenticationFormfrom api.models, Hobbies, UserHobby, PageView

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
            return redirect('main_spa')  # Redirect to a home page or another page
    else:
        form = UserForm()
    
    return render(request, 'signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_spa')  # Redirect to a home page or another page
    else:
        form = UserAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') 

def test_max_heap_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    user = request.user
    max_heap = build_max_heap(user)
    sorted_heap = [(-count, other_user.email) for count, other_user in max_heap]

    return JsonResponse({'max_heap': sorted_heap})

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
            return redirect('main_spa')  # Redirect to a home page or another page
    else:
        form = UserForm()
    
    return render(request, 'signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_spa')  # Redirect to a home page or another page
    else:
        form = UserAuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') 

def test_max_heap_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    user = request.user
    max_heap = build_max_heap(user)
    sorted_heap = [(-count, other_user.email) for count, other_user in max_heap]

    return JsonResponse({'max_heap': sorted_heap})

def get_hobby(request: HttpRequest) -> JsonResponse:
    '''
    Get hobby
    '''
    hobbies = Hobbies.objects.all()
    data = []
    data.append({
        'id': hobbies.id,
        'name': hobbies.name,
        'description': hobbies.description
    })
    return JsonResponse(data, safe=False)

def add_hobby(request: HttpRequest) -> JsonResponse:
    '''
    Add hobby
    '''
    data = json.loads(request.body)
    hobby = Hobbies.objects.create(
        name=data['name'],
        description=data['description']
    )
    return JsonResponse({
        'id': hobby.id,
        'name': hobby.name,
        'description': hobby.description
    })

def update_hobby(request: HttpRequest, hobby_id: int) -> JsonResponse:
    '''
    Update hobby
    '''
    data = json.loads(request.body)
    hobby = Hobbies.objects.get(id=hobby_id)
    return JsonResponse({
        'id': hobby.id,
        'name': hobby.name,
        'description': hobby.description
    })

def delete_hobby(request: HttpRequest, hobby_id: int) -> JsonResponse:
    '''
    Delete hobbies
    '''
    hobby = Hobbies.objects.get(id=hobby_id)
    hobby.delete()
    return JsonResponse({
        'message': 'Hobby deleted successfully'
    })

# PageView views
def page_view(request: HttpRequest) -> JsonResponse:
    page_view = PageView.objects.first()
    page_view.count += 1
    page_view.save()
    return JsonResponse({'count': page_view.count})

# UserHobby
def user_hobby_get(request: HttpRequest) -> JsonResponse:
    user_hobbies = UserHobby.objects.all()
    return JsonResponse({'user_hobbies': list(user_hobbies.values())})

def user_hobby_post(request: HttpRequest) -> JsonResponse:
    user = request.POST.get('user_id')
    hobby = request.POST.get('hobby_id')
    
def user_hobby_delete(request: HttpRequest) -> JsonResponse:
    user= request.POST.get('user_id')
    hobby = request.POST.get('hobby_id')

def user_hobby_put(request: HttpRequest) -> JsonResponse:
    user= request.POST.get('user_id')
    hobby= request.POST.get('hobby_id')