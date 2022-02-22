from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import Product, ProductType
from .serializers import ProductSerializer, ProductTypeSerializer


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductSerializer


class ProductTypeListCreateAPIView(ListCreateAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer


# Api for listing and create a Product
class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ProductType_id=request.data.get("ProductType"))
            return Response({"detail": "insertion is done "}, status=HTTP_200_OK)
        raise ValidationError({"error": " data not correct"})


# this api for (get produit by id )  , upadting a produit and finally delleting
class ProductGetPutDelete(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update(self, request, pk=None, *args, **kwargs):
        product = Product.objects.get(pk=self.kwargs.get('pk'))

        serializer = self.get_serializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save(ProductType_id=request.data.get("ProductType"))
            return Response({"detail": "updating  is done "}, status=HTTP_200_OK)
        raise ValidationError({"error": " data not correct"})
