from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from .models import PageView, User, Hobbies, UserHobby, Friendship

def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

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
    user_id = request.POST.get('user_id')
    hobby_id = request.POST.get('hobby_id')
    
def user_hobby_delete(request: HttpRequest) -> JsonResponse:
    user_id = request.POST.get('user_id')
    hobby_id = request.POST.get('hobby_id')

def user_hobby_put(request: HttpRequest) -> JsonResponse:
    user_id = request.POST.get('user_id')
    hobby_id = request.POST.get('hobby_id')