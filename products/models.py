from django.db import models


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    nm_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    reviews_count = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.name} - {self.discounted_price} ₽"
