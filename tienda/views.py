from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status
from tienda.models import *
from tienda.serializers import *

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
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
    
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def tienda1_list(request):
    if request.method == 'GET':
        tienda1 = Tienda1.objects.all()
        tienda_serializer = Tienda1Serializer(tienda1, many=True)
        return Response(tienda_serializer.data)
    elif request.method == 'POST':
        tienda1_serializer = Tienda1Serializer(data=request.data)
        if tienda1_serializer.is_valid():
            tienda1_serializer.save()
            return Response(tienda1_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tienda1_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def tienda2_list(request):
    if request.method == 'GET':
        tienda2 = Tienda2.objects.all()
        tienda_serializer = Tienda2Serializer(tienda2, many=True)
        return Response(tienda_serializer.data)
    elif request.method == 'POST':
        tienda2_serializer = Tienda2Serializer(data=request.data)
        if tienda2_serializer.is_valid():
            tienda2_serializer.save()
            return Response(tienda2_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tienda2_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def tienda3_list(request):
    if request.method == 'GET':
        tienda3 = Tienda3.objects.all()
        tienda_serializer = Tienda3Serializer(tienda3, many=True)
        return Response(tienda_serializer.data)
    elif request.method == 'POST':
        tienda3_serializer = Tienda3Serializer(data=request.data)
        if tienda3_serializer.is_valid():
            tienda3_serializer.save()
            return Response(tienda3_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tienda3_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
def tienda4_list(request):
    if request.method == 'GET':
        tienda4 = Tienda4.objects.all()
        tienda_serializer = Tienda4Serializer(tienda4, many=True)
        return Response(tienda_serializer.data)
    elif request.method == 'POST':
        tienda4_serializer = Tienda4Serializer(data=request.data)
        if tienda4_serializer.is_valid():
            tienda4_serializer.save()
            return Response(tienda4_serializer.data, status=status.HTTP_201_CREATED)
        return Response(tienda4_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
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
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
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
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
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