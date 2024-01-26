from django.contrib import admin
from products.models import Product
from products.models import Customer  # criado no exercício 01

# Register your models here.

admin.site.site_header = "Trybe Products E-commerce"
admin.site.register(Product)
admin.site.register(Customer)
