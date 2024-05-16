from django.db import models

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # Outros campos necessários para o usuário

    def __str__(self):
        return self.username