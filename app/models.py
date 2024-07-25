from django.db import models
from core.helpers import nullable
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
    

class MenuItem(models.Model):
    name = models.CharField(max_length=100, unique=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE,related_name='items')
    url = models.CharField(max_length= 250, **nullable)
    url_name = models.CharField(max_length=100, **nullable)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, **nullable, related_name='child')

    def __str__(self) -> str:
        return self.name
    
    def get_url(self):
        if self.url_name:
            return reverse(self.url_name)
        return self.url
    