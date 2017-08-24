from rest_framework import generics

from cart.models import CartItem
from cart.serializers import CartItemSerializer


class ItemListView(generics.ListAPIView):

    serializer_class = CartItemSerializer

    def get_queryset(self):
        return self.request.user.cart.items.all()


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
