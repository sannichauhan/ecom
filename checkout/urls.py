from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_page, name='home'),
    path('buy/<int:product_id>/', views.create_checkout_session, name='buy'),
    path('success/', views.payment_success, name='success'),
]