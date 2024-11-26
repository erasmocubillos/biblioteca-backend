from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='libros')
    archivo_pdf = models.FileField(upload_to='libros/')
    preguntas = models.JSONField(default=list)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
