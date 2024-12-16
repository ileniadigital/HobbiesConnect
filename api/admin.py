from django.contrib import admin
from .models import PageView, User, Hobbies, Friendship, UserHobby
# Register your models here.
admin.site.register(User)
admin.site.register(PageView)
admin.site.register(Hobbies)
admin.site.register(Friendship)
admin.site.register(UserHobby)