from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.TextChoices):
    USER = 'user', 'User'
    MANAGER = 'manager', 'Manager'
    ADMIN = 'admin', 'Admin'

class CustomUserModel(AbstractUser):
    middle_name = models.CharField(max_length=30, blank=True)
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER
    )

    @property
    def is_manager(self):
        return self.role == self.Role.MANAGER
    
    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN or self.is_superuser
    
    class Meta:
        db_table = 'users'

