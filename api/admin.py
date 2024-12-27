from django.contrib import admin
from .models import PageView, User, Hobbies, UserHobby, Friendship

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'dob', 'is_staff', 'is_active')

class PageViewAdmin(admin.ModelAdmin):
    list_display = ('count',)

class HobbiesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class UserHobbyAdmin(admin.ModelAdmin):
    list_display = ('user', 'hobby')

class FriendshipAdmin(admin.ModelAdmin):
    list_display = ('user', 'friend', 'status', 'accepted', 'created_at')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(PageView, PageViewAdmin)
admin.site.register(Hobbies, HobbiesAdmin)
admin.site.register(UserHobby, UserHobbyAdmin)
admin.site.register(Friendship, FriendshipAdmin)