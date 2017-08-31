from rest_framework import serializers

from cart.models import CartItem
from shop.serializers import ItemSerializer


class CartItemSerializer(serializers.ModelSerializer):

    item = ItemSerializer()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ('item', 'quantity', 'photo')
        read_only_field = ('item', 'photo')

    def get_photo(self, cart_item):
        request = self.context.get('request')
        try:
            photo = cart_item.item.product.image.url
            return request.build_absolute_uri(photo)
        except ValueError:
            # this product has no avatar
            return None


class CartItemEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ('quantity',)
