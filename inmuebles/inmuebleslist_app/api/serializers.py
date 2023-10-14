from rest_framework import serializers
from inmuebleslist_app.models import Inmueble



class InmuebleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    direccion = serializers.CharField()
    pais = serializers.CharField()
    descripcion = serializers.CharField()
    imagen = serializers.CharField()
    active = serializers.BooleanField()
    
    def create(self, validate_data):
        return Inmueble.objects.create(**validate_data)
    
    def update(self, instance, validate_data):
        instance.direccion = validate_data.get('direccion', instance.direccion)
        instance.pais = validate_data.get('pais', instance.pais)
        instance.descripcion = validate_data.get('descripcion', instance.descripcion)
        instance.imagen = validate_data.get('imagen', instance.imagen)
        instance.active = validate_data.get('active', instance.active)
        instance.save()
        return instance