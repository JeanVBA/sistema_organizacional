from django.contrib import admin
from .models import Position, Branch, Employee, Project, EmployeeProject

# Register your models here.
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'hierarchical', 'descricao')
    search_fields = ['name']

admin.site.register(Position, PositionAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'director', 'date_creation')
    search_fields = ('name','director')

admin.site.register(Branch, BranchAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'position', 'branch', 'supervisor', 'admission_date', 'active')
    search_fields = ['name']

admin.site.register(Employee, EmployeeAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'start_date', 'end_date', 'project_manager', 'branch')
    search_fields = ['name']

admin.site.register(Project, ProjectAdmin)

class EmployeeProjectAdmin(admin.ModelAdmin):
    list_display = ('employee', 'project', 'function_in_project')
    search_fields = ['employee', 'project', 'function_in_project']

admin.site.register(EmployeeProject, EmployeeProjectAdmin)