from django.urls import path
from . import views

urlpatterns = [
    path("", views.checkout, name="checkout"),
    path("checokut_success/<order_number>", views.checkout_success, name="checkout_success"),
]
