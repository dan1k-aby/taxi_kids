from django.db import models


class Voditeli(models.Model):
    Name = models.CharField("Имя", max_length=15)
    Sure_name = models.CharField("Фамилия", max_length=15)
    Date_of_birth = models.CharField("Дата рождения", max_length=10)
    number = models.CharField("Номер телефона", max_length=20)
    Created = models.DateTimeField("Дата регистрации", auto_now=True)
    Auto = models.TextField("Автомобиль", max_length=20)
    Auto_number = models.CharField("госномер", max_length=10)
    class Meta:
        ordering = ("id",)