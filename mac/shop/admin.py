from django.contrib import admin

# Register your models here.
from .models import Product,Contact,Orders,OrderUpdates

admin.site.register(Product)     #WE register our first table(or model) here
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdates)
