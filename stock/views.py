from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductInStockSerializer, RotationSerializer, ProductInRotationSerializer
from .models import Rotation, ProductInRotation, Product

class ProductsInStock(APIView):
    """
    View to get list of all products
    """
    def get(self, request, format=None):
        user = request.user
        user_stock = user.stock
        productos_in_stock = user_stock.productinstock_set.all()

        return Response(
            ProductInStockSerializer(productos_in_stock, many=True).data
        )
    

class CountProductsInStock(APIView):
    """
    View to get count to al productos in stock
    """
    def get(self, request, format=None):
        user = request.user
        count_products = 0

        products = user.stock.productinstock_set.all()

        for product in products:
            count_products += product.quantity

        return Response({'count': count_products})
    
class RotationUpdate(APIView):
    """
    View to update rotation of dealer
    """
    
    def post(self, request, format=None):
        rotation_products = request.data['rotation_products']
        rotation_id = request.data['rotation_id']
        # get rotation
        rotation = Rotation.objects.get(id=rotation_id)
        # add products to rotation
        for x in rotation_products:
            rotation.productinrotation_set.create(
                product=Product.objects.get(id=int(x['id'])), quantity=x['quantity']
            )
            
        rotation.pending = False
        rotation.save()
        
        return Response()
    
class RotationDetail(APIView):
    """
    View to get rotation details
    """
    def get(self, request, id=None, format=None):
        rotation = Rotation.objects.get(id=id)
        products_in_rotation = rotation.productinrotation_set.all()

        return Response(
            ProductInRotationSerializer(products_in_rotation, many=True).data
        )
        
class RotationList(APIView):
    """
    View to get rotation list
    """
    def get(self, request, format=None):
        user = request.user
        rotation_list = user.rotation_set.filter(pending=False)

        return Response(
            RotationSerializer(rotation_list, many=True).data
        )
        
class RotationPending(APIView):
    """
    View to get rotation list
    """
    def get(self, request, format=None):
        user = request.user
        rotation_list = user.rotation_set.filter(pending=True)

        return Response(
            RotationSerializer(rotation_list, many=True).data
        )    