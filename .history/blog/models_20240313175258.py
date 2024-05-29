from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')  # Corregido aquí
    description = models.CharField(max_length=255, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta: 
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField(default='null', verbose_name='Imagen',)
    public = models.BooleanField(verbose_name='¿Publicado?')  # Corregido aquí
    user = models.ForeignKey(User,editable=False,verbose_name='Usuario', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categorías', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')


#editable=False, se pone para crear el articulo el permiso denegado a un usuario si le quitamos el usuario tendria el permiso de publicar articulos 
    class Meta: 
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículos'

    def __str__(self):
        return self.title
