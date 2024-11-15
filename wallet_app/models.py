from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Spending(models.Model):
    name = models.CharField(max_length=255)
    charge = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Purchases(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    day = models.ForeignKey('Days', on_delete=models.SET_NULL, null=True)


class Days(models.Model):
    name = models.CharField(max_length=255)
