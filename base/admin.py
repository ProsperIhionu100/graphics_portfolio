from django.contrib import admin

from . models import Company, Project

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    
    prepopulated_fields = { 'slug' : ('name',)}    

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    
    prepopulated_fields = { 'slug' : ('name',)}

# Register your models here.


