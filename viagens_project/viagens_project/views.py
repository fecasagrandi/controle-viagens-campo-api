from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Destino, Transporte, Categoria, Viagem
from .serializers import UsuarioSerializer, DestinoSerializer, TransporteSerializer, CategoriaSerializer, ViagemSerializer

@api_view(['POST'])
def inserirUsuario(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listarUsuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def atualizarUsuario(request, pk):
    try:
        usuario = Usuario.objects.get(id=pk)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UsuarioSerializer(usuario, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletarUsuario(request, pk):
    try:
        usuario = Usuario.objects.get(id=pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def inserirDestino(request):
    serializer = DestinoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listarDestinos(request):
    destinos = Destino.objects.all()
    serializer = DestinoSerializer(destinos, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def atualizarDestino(request, pk):
    try:
        destino = Destino.objects.get(id=pk)
    except Destino.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = DestinoSerializer(destino, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletarDestino(request, pk):
    try:
        destino = Destino.objects.get(id=pk)
        destino.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Destino.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def inserirTransporte(request):
    serializer = TransporteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listarTransportes(request):
    transportes = Transporte.objects.all()
    serializer = TransporteSerializer(transportes, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def atualizarTransporte(request, pk):
    try:
        transporte = Transporte.objects.get(id=pk)
    except Transporte.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TransporteSerializer(transporte, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletarTransporte(request, pk):
    try:
        transporte = Transporte.objects.get(id=pk)
        transporte.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Transporte.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def inserirCategoria(request):
    serializer = CategoriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listarCategorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def atualizarCategoria(request, pk):
    try:
        categoria = Categoria.objects.get(id=pk)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CategoriaSerializer(categoria, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletarCategoria(request, pk):
    try:
        categoria = Categoria.objects.get(id=pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def inserirViagem(request):
    serializer = ViagemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listarViagens(request):
    viagens = Viagem.objects.all()
    serializer = ViagemSerializer(viagens, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def atualizarViagem(request, pk):
    try:
        viagem = Viagem.objects.get(id=pk)
    except Viagem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ViagemSerializer(viagem, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletarViagem(request, pk):
    try:
        viagem = Viagem.objects.get(id=pk)
        viagem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Viagem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
