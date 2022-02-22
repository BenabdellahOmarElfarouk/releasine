from rest_framework import serializers

from .models import AttributeValue, ProductType, Attribute, AssignedAttribute, Product


class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = ['id', 'Name', 'Boolean', 'Date']


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'Name', 'created_at']


class AttributeSerializer(serializers.ModelSerializer):
    AttributeValue = AttributeValueSerializer(read_only=True)
    ProductType = ProductTypeSerializer(read_only=True)

    class Meta:
        model = Attribute
        fields = ['id', 'Name', 'Type', 'AttributeValue', 'ProductType']


class ProductSerializer(serializers.ModelSerializer):
    ProductType = ProductTypeSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'Name', 'created_at', 'ProductType']


class AssignedAttributeSerializer(serializers.ModelSerializer):
    AttributeValue = AttributeValueSerializer(read_only=True)
    Product = ProductSerializer(read_only=True)

    class Meta:
        model = AssignedAttribute
        fields = ['id', 'AttributeValue', 'Product']
