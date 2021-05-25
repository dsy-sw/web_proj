from django.db import models
from django.utils.text import slugify


class User(models.Model):
    username     = models.CharField(max_length = 20, verbose_name='username',db_column='username')
    email   = models.EmailField(max_length = 20, verbose_name='email',db_column='email')
    password    = models.CharField(max_length = 20, verbose_name='password', db_column='password')

    class Meta:
        db_table = 'users'
        verbose_name = 'user'

    def __str__(self):
        return self.username
        #문자열 반환
