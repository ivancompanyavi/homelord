from django.db import models


class Cart(models.Model):

    description = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now=True)


class Registry(models.Model):

    description = models.CharField(max_length=50)
    creation_date = models.DateField(auto_now=True)
    quantity = models.IntegerField(default=1)
    ppu = models.FloatField(default=0.0)
    cart = models.ForeignKey(Cart, blank=True, null=True)


class Goal(models.Model):

    description = models.CharField(max_length=50)
    from_date = models.DateField(auto_now=True)
    to_date = models.DateField()
    objective = models.FloatField()