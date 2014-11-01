from django.db import models


class Cart(models.Model):

    description = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now=True)


class Registry(models.Model):

    description = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now=True)
    quantity = models.IntegerField()
    ppu = models.FloatField()
    cart = models.ForeignKey(Cart)


class Goal(models.Model):

    description = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    objective = models.FloatField()