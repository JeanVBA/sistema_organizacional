from rest_framework import viewsets
from .models import Position, Branch, Employee, Project, EmployeeProject
from .serializers import *

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class EmployeeProjectViewSet(viewsets.ModelViewSet):
    queryset = EmployeeProject.objects.all()
    serializer_class = EmployeeProjectSerializer
