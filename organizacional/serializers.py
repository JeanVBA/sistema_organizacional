from rest_framework import serializers
from .models import Position, Branch, Employee, Project, EmployeeProject

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class EmployeeProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProject
        fields = '__all__'
