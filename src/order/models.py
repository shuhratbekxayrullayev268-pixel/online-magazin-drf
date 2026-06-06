from django.db import models
from apps.shop.models import Product
from apps.users.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.first_name} - {self.product.name_uz}"


class OrderStatus(models.TextChoices):
    NEW = 'new', 'New'
    IN_PROGRESS = 'in_progress', 'In Progress'
    COMPLATED = 'completed', 'Completed'
    CANCELLED = 'cancelled', 'Cancelled'

class Order(models.Model):    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField(default=0)
    address = models.CharField(max_length=500)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.NEW)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user.first_name}"


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    amount = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product.name_uz} ({self.amount})"
