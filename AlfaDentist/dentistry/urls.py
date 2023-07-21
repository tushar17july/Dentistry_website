from django.contrib import admin
from django.urls import path
from dentistry import views

urlpatterns = [
    path('',views.index, name='home'),
    path('pricing',views.pricing, name='pricing'),
    path('services',views.services, name='services'),
    path('contact',views.contact, name='contact'),
]
