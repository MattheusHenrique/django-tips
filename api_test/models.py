from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20, unique=True)
    # Acho que seria melhor usar inteiro e tratar as duas ultimas casas (melhor para realizar as operações)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    quantity_in_stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
