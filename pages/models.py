from django.db import models
#from numpy import unique
from ckeditor.fields import RichTextField
# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido") # Adjust max_length as needed
    slug = models.CharField(unique=True, max_length=150, verbose_name="URL amigable")

    visible = models.BooleanField(verbose_name="¿Visible?")


    order = models.IntegerField(default=0,verbose_name="Orden")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creacion")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Actualizacion")

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "paginas"

    def __str__(self):
        return self.title
