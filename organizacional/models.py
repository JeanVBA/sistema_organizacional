from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class Position(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    hierarchical = models.IntegerField(null=False,
                                       validators=[
            MinValueValidator(1),
            MaxValueValidator(4)
        ])
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Branch(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255, null=True, blank=True)
    director = models.ForeignKey('Employee', on_delete=models.SET_NULL,
                                null=True, blank=True, related_name='branch_director')
    date_creation = models.DateField()

    def __str__(self):
        return str(self.name)

class Employee(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    position = models.ForeignKey(Position, on_delete=models.PROTECT, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT, null=True, blank=True)
    supervisor = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subordinates')
    admission_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # username ainda é necessário

    def __str__(self):
        return str(self.name)

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    project_manager = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='managed_projects')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class EmployeeProject(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    function_in_project = models.CharField(max_length=100)

    class Meta:
        unique_together = ('employee', 'project')
