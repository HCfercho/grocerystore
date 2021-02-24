from rest_framework import serializers
from tienda.models import *

class Tienda1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda1
        fields = '__all__'
        
class Tienda2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda1
        fields = '__all__'

class Tienda3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda1
        fields = '__all__'

class Tienda4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda1
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
class StockEnTiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock_En_Tienda
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class SubCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoria
        fields = '__all__'