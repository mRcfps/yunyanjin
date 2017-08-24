from rest_framework import serializers

from shop.models import Product, Photo, Item


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'info', 'items')


class ProductPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('product', 'photo')


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('product', 'price', 'unit', 'stock')
