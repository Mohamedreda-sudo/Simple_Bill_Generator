
from django.db import models

class BoughtItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bought_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
