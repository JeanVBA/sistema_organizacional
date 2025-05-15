from rest_framework import serializers
from .models import Cargo, Filial, Usuario, Projeto, UsuarioProjeto

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = '__all__'

class UsuarioProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioProjeto
        fields = '__all__'
