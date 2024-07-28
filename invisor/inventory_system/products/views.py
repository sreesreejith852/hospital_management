from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Products, Variants, SubVariants
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        product = Products.objects.create(
            ProductName=data['name'],
            ProductID=self.generate_unique_product_id(),  
            ProductCode=self.generate_unique_product_code(),  
            CreatedUser=request.user
        )
        for variant in data.get('variants', []):
            variant_obj = Variants.objects.create(Product=product, VariantName=variant['name'])
            for option in variant.get('options', []):
                SubVariants.objects.create(Variant=variant_obj, OptionName=option)
        serializer = self.get_serializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def add_stock(self, request, pk=None):
        product = self.get_object()
        data = request.data
        for variant in product.variants.all():
            for subvariant in variant.subvariants.all():
                if subvariant.id == data['subvariant_id']:
                    subvariant.Stock += data['stock']
                    subvariant.save()
                    product.TotalStock += data['stock']
                    product.save()
                    return Response({'status': 'stock added'}, status=status.HTTP_200_OK)
        return Response({'error': 'subvariant not found'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def remove_stock(self, request, pk=None):
        product = self.get_object()
        data = request.data
        for variant in product.variants.all():
            for subvariant in variant.subvariants.all():
                if subvariant.id == data['subvariant_id']:
                    if subvariant.Stock >= data['stock']:
                        subvariant.Stock -= data['stock']
                        subvariant.save()
                        product.TotalStock -= data['stock']
                        product.save()
                        return Response({'status': 'stock removed'}, status=status.HTTP_200_OK)
                    else:
                        return Response({'error': 'not enough stock'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'subvariant not found'}, status=status.HTTP_400_BAD_REQUEST)

    def generate_unique_product_id(self):
        pass

    def generate_unique_product_code(self):
        pass

