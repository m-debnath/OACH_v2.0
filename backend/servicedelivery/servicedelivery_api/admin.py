from django.contrib import admin
from .models import Order, OrderItem, InstalledAsset

admin.site.site_header = 'Service Delivery Backend administration'
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(InstalledAsset)