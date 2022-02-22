from django.db import models
from django.utils import timezone

class AttributeValue(models.Model):
    Name = models.CharField(max_length=50)
    Boolean = models.models.BooleanField()
    Date = models.DateField()

    def __str__(self):
        return self.Name

class Attribute(models.Model):
    Name = models.CharField(max_length=50)
    Type = models.CharField(max_length=50)
    AttributeValue = models.ForeignKey(to='AttributeValue', on_delete=models.CASCADE)
    ProductType = models.ForeignKey(to='ProductType', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class AssignedAttribute(models.Model):
    AttributeValue = models.ForeignKey(to='AttributeValue', on_delete=models.CASCADE)
    Product = models.ForeignKey(to='Product', on_delete=models.CASCADE)



class ProductType(models.Model):
    Name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Name


class Product(models.Model):
    Name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
    ProductType = models.ForeignKey(to='ProductType', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name