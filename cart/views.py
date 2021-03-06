from rest_framework import generics

from .models import Cart, CartEntry
from .serializers import CartEntryEditSerializer, CartEntrySerializer


class EntryListView(generics.ListAPIView):

    serializer_class = CartEntrySerializer

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart.entries.all()


class EntryDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = CartEntry.objects.all()
    serializer_class = CartEntryEditSerializer
