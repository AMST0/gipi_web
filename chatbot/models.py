from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Kullanıcı")
    message = models.TextField(verbose_name="Mesaj")
    response = models.TextField(verbose_name="GIPI")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Tarih")

    def __str__(self):
        return f'{self.user.username}: {self.message}'