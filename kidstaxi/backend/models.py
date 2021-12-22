from django.db import models


class Voditeli(models.Model):
    Name_vod = models.CharField("Имя", max_length=15)
    Sure_name = models.CharField("Фамилия", max_length=15)
    Date_of_birth = models.CharField("Дата рождения", max_length=10)
    number = models.CharField("Номер телефона", max_length=20)
    Created = models.DateTimeField("Дата регистрации", auto_now_add=True)
    Auto = models.TextField("Автомобиль", max_length=20)
    Auto_number = models.CharField("госномер", max_length=10)
    
    class Meta:
        ordering = ("id",)


class People(models.Model):
    Name_man = models.CharField("Имя", max_length=15)
    Sure_name = models.CharField("Фамилия", max_length=15)
    Number = models.CharField("Номер телефона", max_length=20)
    
    class Meta:
        ordering = ("id",)

class Dispetchery(models.Model):
    Name = models.CharField("Имя", max_length=15)
    Sure_name = models.CharField("Фамилия", max_length=15)
    Date_of_birth = models.CharField("Дата рождения", max_length=10)
    Number = models.CharField("Номер телефона", max_length=15)
    Created = models.DateTimeField("Дата регистрации", auto_now_add=True)
    Email = models.EmailField("email")

    class Meta:
        ordering = ("id",)


class Order(models.Model):
    Created = models.DateTimeField("Дата", auto_now_add=True)
    Name_people = models.ForeignKey(
        People, on_delete=models.CASCADE, related_name="orders", null=True)
    Name_vodil = models.ForeignKey(
        Voditeli, on_delete=models.CASCADE, related_name="orders", null=True)
    Marshrut = models.CharField("Маршрут", max_length=30)
    Status = models.CharField("Статус", max_length=15)
    Order_number = models.CharField("Номер заказа", max_length=15)
    
    class Meta:
        ordering = ("id",)