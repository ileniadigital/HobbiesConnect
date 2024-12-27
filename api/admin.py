from django.contrib import admin
from .models import PageView, User, Hobbies, UserHobby, Friendship
# Register your models here.
admin.site.register(User)
admin.site.register(PageView)
admin.site.register(Hobbies)
admin.site.register(UserHobby)
admin.site.register(Friendship)
