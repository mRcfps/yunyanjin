from rest_framework import serializers

from cart.models import CartItem
from shop.serializers import ItemSerializer


class CartItemSerializer(serializers.ModelSerializer):

    item = ItemSerializer()

    class Meta:
        model = CartItem
        fields = ('item', 'quantity')
