from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, \
    PermissionsMixin


class CustomUserManager(BaseUserManager):
    """Менеджер пользователей."""

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Email is not required')
        email = self.normalize_email(email)
        user = self.model(email=email)
        # Храниться в зашифрованном виде
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    username = None
    # Поле в качестве имени пользователя
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )

    def __str__(self):
        return self.email
