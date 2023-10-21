from rest_framework.response import Response
from inmuebleslist_app.models import Edificacion, Empresa, Comentario
from inmuebleslist_app.api.serializers import EdificacionSerializer, EmpresaSerializer, ComentarioSerializer
#from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins


class ComentarioList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class EmpresaAV(APIView):
    def get(self, request):
        empresas = Empresa.objects.all()
        serializer = EmpresaSerializer(empresas, many=True, context = {'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmpresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class EmpresaDetalleAV(APIView):
    def get(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'Error: Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmpresaSerializer(empresa, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error': 'Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmpresaSerializer(empresa, data=request.data, context={'request', request})
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            empresa = Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'Error: Empresa no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EdificacionAV(APIView):
    def get(self, request, format=None):
        inmuebles = Edificacion.objects.all()
        serializer = EdificacionSerializer(inmuebles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EdificacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EdificacionDetalleAV(APIView):
    def get(self, request, pk):
        try:
            inmueble = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'Error: Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EdificacionSerializer(inmueble)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            inmueble = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'Error: Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EdificacionSerializer(inmueble, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            inmueble = Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response({'Error: Inmueble no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        inmueble.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def inmueble_list(request):
#     if request.method == 'GET':
#         inmuebles = Inmueble.objects.all()
#         serializer = InmuebleSerializer(inmuebles, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         de_serializer = InmuebleSerializer(data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data, status=201)
#         return Response(de_serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def inmueble_detalle(request, pk):
#     if request.method == 'GET':
#         try:
#             inmueble = Inmueble.objects.get(pk=pk)
#             serializer = InmuebleSerializer(inmueble)
#             return Response(serializer.data)
#         except Inmueble.DoesNotExist:
#             return Response({'Error: El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'PUT':
#         inmueble = Inmueble.objects.get(pk=pk)
#         de_serializer = InmuebleSerializer(inmueble, data=request.data)
#         if de_serializer.is_valid():
#             de_serializer.save()
#             return Response(de_serializer.data, status=201)
#         else:
#             return Response(de_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         try:
#             inmueble = Inmueble.objects.get(pk=pk)
#             inmueble.delete()
#         except Inmueble.DoesNotExist:
#             return Response({'Error: El inmueble no existe'}, status=status.HTTP_404_NOT_FOUND)
#         return Response({"data": True},status=status.HTTP_204_NO_CONTENT)