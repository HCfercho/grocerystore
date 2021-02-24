from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from tienda.models import *
from tienda.serializers import *

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        products = Producto.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return Response(products_serializer.data)
    elif request.method == 'POST':
        product_serializer = ProductSerializer(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def tienda1_list(request):
    if request.method == 'POST':
        tienda1_serializer = Tienda1Serializer(data=request.data)
        if tienda1_serializer.is_valid():
            tienda1_serializer.save()
            return Response(tienda1_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tienda1_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def tienda2_list(request):
    if request.method == 'POST':
        tienda2_serializer = Tienda2Serializer(data=request.data)
        if tienda2_serializer.is_valid():
            tienda2_serializer.save()
            return Response(tienda2_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tienda2_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def tienda3_list(request):
    if request.method == 'POST':
        tienda3_serializer = Tienda3Serializer(data=request.data)
        if tienda3_serializer.is_valid():
            tienda3_serializer.save()
            return Response(tienda3_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tienda3_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def tienda4_list(request):
    if request.method == 'POST':
        tienda4_serializer = Tienda4Serializer(data=request.data)
        if tienda4_serializer.is_valid():
            tienda4_serializer.save()
            return Response(tienda4_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tienda4_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def stock_en_tienda_list(request):
    if request.method == 'GET':
        stocks = Stock_En_Tienda.objects.all()
        stocks_serializer = StockEnTiendaSerializer(stocks, many=True)
        return Response(stocks_serializer.data)
    elif request.method == 'POST':
        stock_serializer = StockEnTiendaSerializer(data=request.data)
        if stock_serializer.is_valid():
            stock_serializer.save()
            return Response(stock_serializer.data, status=status.HTTP_201_CREATED)
        return Response(stock_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
@api_view(['GET','POST'])
def categoria_list(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        categorias_serializer = CategoriaSerializer(categorias, many=True)
        return Response(categorias_serializer.data)
    elif request.method == 'POST':
        categoria_serializer = CategoriaSerializer(data=request.data)
        if categoria_serializer.is_valid():
            categoria_serializer.save()
            return Response(categoria_serializer.data, status=status.HTTP_201_CREATED)
        return Response(categoria_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
def subcategoria_list(request):
    if request.method == 'GET':
        subcategorias = SubCategoria.objects.all()
        subcategorias_serializer = CategoriaSerializer(subcategorias, many=True)
        return Response(subcategorias_serializer.data)
    elif request.method == 'POST':
        subcategoria_serializer = SubCategoriaSerializer(data=request.data)
        if subcategoria_serializer.is_valid():
            subcategoria_serializer.save()
            return Response(subcategoria_serializer.data, status=status.HTTP_201_CREATED)
        return Response(subcategoria_serializer.errors, status=status.HTTP_400_BAD_REQUEST)