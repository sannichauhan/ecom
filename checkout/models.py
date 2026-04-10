from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()  # Price in cents (Stripe requirement)

    def price_display(self):
        return self.price / 100
    
    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    stripe_checkout_id = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=20, default='pending') # pending, paid
    created_at = models.DateTimeField(auto_now_add=True)