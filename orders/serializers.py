from rest_framework import serializers

from shop.serializers import ItemSerializer

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    item = ItemSerializer()

    class Meta:
        model = OrderItem
        fields = ('item', 'quantity')
        read_only_fields = ('item',)


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('order_id', 'items', 'status', 'destination', 'phone')
