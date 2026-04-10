
from django.contrib import admin
from .models import Product, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # What columns to show in the list view
    list_display = ('name', 'get_price_usd')
    
    def get_price_usd(self, obj):
        return f"${obj.price / 100:.2f}"
    get_price_usd.short_description = 'Price (USD)'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # Show key details at a glance
    list_display = ('id', 'product', 'quantity', 'status', 'created_at')
    
    # Add filters on the right side
    list_filter = ('status', 'created_at')
    
    # Make Stripe ID and status readonly so you don't break logic manually
    readonly_fields = ('stripe_checkout_id', 'created_at')
    
    # Search by Stripe ID or Product Name
    search_fields = ('stripe_checkout_id', 'product__name')