from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя игрока')
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Баланс игрока')
    age = models.IntegerField(verbose_name='Возраст игрока')

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

    def __str__(self):
        return self.title
