from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class PageView(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Page view count: {self.count}"


class User(AbstractUser):
    """
    Custom User model inheriting Django's AbstractUser with email as the unique identifier.
    """
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dob = models.DateField()
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Avoid reverse accessor clashes
        blank=True,
        help_text='The groups this user belongs to.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Avoid reverse accessor clashes
        blank=True,
        help_text='Specific permissions for this user.',
    )

    USERNAME_FIELD = 'email' #username is emai
    REQUIRED_FIELDS = ['first_name', 'last_name']


