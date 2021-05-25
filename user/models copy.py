from django.db import models

class User(models.Model):
    username     = models.CharField(max_length = 20, verbose_name='username',db_column='username')
    name   = models.CharField(max_length = 20, verbose_name='name',db_column='first_name')
    password    = models.CharField(max_length = 20, verbose_name='password', db_column='password')
    addr   = models.CharField(max_length = 255, verbose_name='addr', db_column='last_name')

    class Meta:
        db_table = 'users'