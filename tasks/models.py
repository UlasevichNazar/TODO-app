from django.contrib.auth import get_user_model
from django.db import models

from config import settings


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='tasks')
    title = models.CharField('Заголовок', max_length=200)
    description = models.TextField('Описание', null=True, blank=True)
    complete = models.BooleanField('Выполнено', default=False)
    created = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
        verbose_name = 'Задачa'
        verbose_name_plural = 'Задачи'
