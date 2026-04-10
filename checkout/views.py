
from django.shortcuts import render, redirect

import stripe
from django.conf import settings
from .models import Product, Order

stripe.api_key = settings.STRIPE_SECRET_KEY

def product_page(request):
    products = Product.objects.all()
    orders = Order.objects.filter(status='paid').order_by('-created_at')
    return render(request, 'index.html', {'products': products, 'orders': orders})

def create_checkout_session(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        quantity = int(request.POST.get('quantity', 1))

        # 1. Create a Stripe Checkout Session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': product.name},
                    'unit_amount': product.price,
                },
                'quantity': quantity,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/success/') + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri('/'),
        )

        # 2. Create a pending order to track the attempt
        Order.objects.create(
            product=product,
            quantity=quantity,
            stripe_checkout_id=checkout_session.id,
            status='pending'
        )

        return redirect(checkout_session.url, code=303)

# This view will be called by Stripe after payment is successful and will update the order status to 'paid'.
def payment_success(request):
    session_id = request.GET.get('session_id')
    # Prevent double processing: Find order and mark as paid
    order = Order.objects.get(stripe_checkout_id=session_id)
    
    # Simple logic to ensure we only update once
    if order.status != 'paid':
        order.status = 'paid'
        order.save()
        
    return redirect('home')
