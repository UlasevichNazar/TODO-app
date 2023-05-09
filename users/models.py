from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import CustomManager


class User(AbstractUser):
    username = models.CharField('Никнейм', max_length=255, unique=True)
    email = models.EmailField('Почта', unique=True, blank=True, null=True)
    phone_number = PhoneNumberField("Телефон", unique=True, blank=True, null=True)
    USERNAME_FIELD = 'username'
    objects = CustomManager()


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def __str__(self):
        return f"{self.username}"
