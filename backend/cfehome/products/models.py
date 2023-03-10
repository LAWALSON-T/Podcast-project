from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length= 120)
    Content = models.TextField(blank= True, null= True)
    Email = models.EmailField(max_length=100)
    Date = models.DateField(auto_now_add= True)