from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.email


class School(models.Model):
    title = models.CharField(max_length=100)
    type_of_sport = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    users = models.ManyToManyField(User)