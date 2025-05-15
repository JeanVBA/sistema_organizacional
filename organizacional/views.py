from rest_framework import viewsets
from .models import Cargo, Filial, Usuario, Projeto, UsuarioProjeto
from .serializers import *

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class FilialViewSet(viewsets.ModelViewSet):
    queryset = Filial.objects.all()
    serializer_class = FilialSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

class UsuarioProjetoViewSet(viewsets.ModelViewSet):
    queryset = UsuarioProjeto.objects.all()
    serializer_class = UsuarioProjetoSerializer
