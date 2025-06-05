from django.db import models
from django_resized import ResizedImageField

# Create your models here.

class Company(models.Model):
    
    name = models.CharField(max_length=250, db_index=True)
    
    desc = models.TextField(blank=True)
    
    slug = models.SlugField(max_length=250, unique=True)
    
    image = ResizedImageField(size=[600, 600], quality=85, upload_to='images/', null=True)
    
    
    class Meta:
        
        verbose_name_plural = 'companies'
        
    def __str__(self):
        
        return self.name
    
class Project(models.Model):
    category = models.ForeignKey(Company, related_name='product', on_delete=models.CASCADE, null=True)
    
    name = models.CharField(max_length=250)
    
    desc = models.TextField(blank=True)
    
    slug = models.SlugField(max_length=250, unique=True, null=True)
    
    image = ResizedImageField(size=[600, 600], quality=85, upload_to='images/', null=True)
    
    class Meta:
        
        verbose_name_plural = 'projects'
        
    def __str__(self):
        
        return self.name