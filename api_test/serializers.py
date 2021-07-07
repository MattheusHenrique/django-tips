from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False)
    price = serializers.DecimalField(required=False, decimal_places=2, max_digits=1000)
    quantity_in_stock = serializers.IntegerField(required=False)

    def create(self, validated_data):
        """ Cria e retorna uma nova instancia de Product """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """ Atualiza um valor ja existente de Product """
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity_in_stock = validated_data('quantity_in_stock', instance.quantity_in_stock)
        instance.save()
        return instance
