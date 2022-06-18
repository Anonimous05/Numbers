from django.db import models

# Create your models here.


class Order(models.Model):
    order_number = models.IntegerField()
    price_usd = models.FloatField()
    delivery_date = models.DateField()
    price_rub = models.FloatField(null=True)

    def __str__(self):
        return self.order_number.__str__()
