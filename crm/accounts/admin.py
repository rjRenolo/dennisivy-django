from django.contrib import admin

from .models import Costumer, Product, Order, Tag

# Register your models here.

admin.site.register(Costumer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)
