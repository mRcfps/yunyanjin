from rest_framework import generics

from shop.models import Product, Photo, Item
from shop.serializers import (ProductDetailSerializer,
                              ProductPhotoSerializer,
                              ItemSerializer)


class ProductDetailView(generics.RetrieveAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ProductPhotosView(generics.ListAPIView):

    serializer_class = ProductPhotoSerializer

    def get_queryset(self):
        product = Product.objects.get(id=self.kwargs['pk'])
        return product.photos.all()


class ProductItemsView(generics.ListAPIView):

    serializer_class = ItemSerializer

    def get_queryset(self):
        product = Product.objects.get(id=self.kwargs['pk'])
        return product.items.all()
