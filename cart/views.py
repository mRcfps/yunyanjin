from rest_framework import generics

from cart.models import Cart, CartEntry
from cart.serializers import CartEntrySerializer, CartEntryEditSerializer


class ItemListView(generics.ListAPIView):

    serializer_class = CartEntrySerializer

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart.entries.all()


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = CartEntry.objects.all()
    serializer_class = CartEntryEditSerializer
