from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    content = models.TextFieldextField(verbose_name="Contenido", max_length=255)  # Adjust max_length as needed
    slug = models.CharField(max_length=150, unique=True, verbose_name="URL amigable")

    visible = models.BooleanField(verbose_name="¿Visible?")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creacion")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizacion")

    class Meta:
        verbose_name = "pagina"
        verbose_name_plural = "paginas"

    def __str__(self):
        return self.title
