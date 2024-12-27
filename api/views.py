import json
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from api.models import Hobbies, UserHobby, PageView

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
    user = request.POST.get('user_id')
    hobby = request.POST.get('hobby_id')
    
def user_hobby_delete(request: HttpRequest) -> JsonResponse:
    user= request.POST.get('user_id')
    hobby = request.POST.get('hobby_id')

def user_hobby_put(request: HttpRequest) -> JsonResponse:
    user= request.POST.get('user_id')
    hobby= request.POST.get('hobby_id')

#Hobbies
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

