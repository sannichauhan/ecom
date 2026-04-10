from django.apps import AppConfig
from django.db.models.signals import post_migrate


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "checkout"
    
    def ready(self):
        # post_migrate signal will run after migrations are applied, ensuring our initial data is seeded
        post_migrate.connect(seed_initial_data, sender=self)

def seed_initial_data(sender, **kwargs):
    # Import is required here to avoid circular imports since models are not loaded at the time of app initialization.
    from .models import Product
    
    products_data = [
        {'name': 'Minimalist Watch', 'price': 499900},
        {'name': 'Leather Journal', 'price': 89900},
        {'name': 'Smart Coffee Mug', 'price': 250000},
    ]

    for item in products_data:
        # update_or_create will ensure we don't create duplicates if the data already exists, making it safe to run multiple times
        Product.objects.update_or_create(
            name=item['name'],
            defaults={'price': item['price']}
        )