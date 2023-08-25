from rest_framework import serializers
from .models import Product, Characteristic

class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    characteristics = CharacteristicSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'file', 'file1', 'user', 'created_at', 'name', 'description', 'characteristics']

    # Override create method to handle nested characteristics
    def create(self, validated_data):
        characteristics_data = validated_data.pop('characteristics', [])
        product = Product.objects.create(**validated_data)

        for char_data in characteristics_data:
            char, _ = Characteristic.objects.get_or_create(**char_data)
            product.characteristics.add(char)

        return product
    def update(self, instance, validated_data):
        characteristics_data = validated_data.pop('characteristics', [])
        instance = super().update(instance, validated_data)

        instance.characteristics.clear()  # Clear existing characteristics of the product

        for char_data in characteristics_data:
            char, _ = Characteristic.objects.get_or_create(**char_data)
            instance.characteristics.add(char)

        return instance
