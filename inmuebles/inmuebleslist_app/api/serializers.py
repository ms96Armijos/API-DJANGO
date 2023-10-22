from rest_framework import serializers
from inmuebleslist_app.models import Edificacion, Empresa, Comentario


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        exclude= ['edificacion']
        #fields = "__all__"

class EdificacionSerializer(serializers.ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    class Meta: #Mapea automaticamente los datos
        model = Edificacion
        fields = "__all__" #mostrar todos los campos
        # fields = ['pais', 'active', 'imagen'] mostrar los campos definidos
        #exclude = ['id'] #excluir el campo definido
        
        
        
class EmpresaSerializer(serializers.ModelSerializer):
    edificacionlist = EdificacionSerializer(many=True, read_only=True)
    #edificacionlist = serializers.StringRelatedField(many=True)
    #edificacionlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #edificacionlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name = 'edificacion-detalle')
    class Meta:
        model = Empresa
        fields = '__all__'

        
        
        
        
        
        
        
        
        
        
        
        
        
    # def get_longitud_direccion(self, object):
    #     cantidad_caracteres = len(object.direccion)
    #     return cantidad_caracteres

    # def validate(self, data):
    #     if data['direccion'] == data['pais']:
    #         raise serializers.ValidationError("La dirección y el país deben ser diferentes")
    #     else:
    #         return data
    # #validaciones individuales con validate y sguido del guion bajo mas el nombre del campo de la clase
    # def validate_imagen(self, data):
    #     if len(data)<2:
    #         raise serializers.ValidationError("La imagen es demasiado corta")
    #     else:
    #         data 





# def column_longitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("La dirección es demasiado corta")

# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     direccion = serializers.CharField(validators=[column_longitud])
#     pais = serializers.CharField()
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validate_data):
#         return Inmueble.objects.create(**validate_data)
    
#     def update(self, instance, validate_data):
#         instance.direccion = validate_data.get('direccion', instance.direccion)
#         instance.pais = validate_data.get('pais', instance.pais)
#         instance.descripcion = validate_data.get('descripcion', instance.descripcion)
#         instance.imagen = validate_data.get('imagen', instance.imagen)
#         instance.active = validate_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['direccion'] == data['pais']:
#             raise serializers.ValidationError("La dirección y el país deben ser diferentes")
#         else:
#             return data
#     #validaciones individuales con validate y sguido del guion bajo mas el nombre del campo de la clase
#     def validate_imagen(self, data):
#         if len(data)<2:
#             raise serializers.ValidationError("La imagen es demasiado corta")
#         else:
#             data 