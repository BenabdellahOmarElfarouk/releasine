from django.contrib import admin

# Register your models here.
from .models import AttributeValue, Attribute, AssignedAttribute, ProductType, Product

admin.site.register(AttributeValue)
admin.site.register(Attribute)
admin.site.register(AssignedAttribute)
admin.site.register(ProductType)
admin.site.register(Product)
