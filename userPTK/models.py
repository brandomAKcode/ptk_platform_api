from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class UserPTK(AbstractUser):
    ADMIN = 'ADM'
    DEALER = 'DEA'
    USER_ROLE = {
        ADMIN: 'Admin',
        DEALER: 'Dealer',
    }
    
    email = models.EmailField(max_length=70, unique=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10, null=True)
    photo = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    role = models.CharField(
        max_length=3,
        choices=USER_ROLE,
        default=DEALER
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'name']
    objects = UserManager()

    def __str__(self):
        return f"{self.name} ({self.email})"