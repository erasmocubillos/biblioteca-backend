from rest_framework import serializers
from .models import Categoria, Libro


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']


class LibroSerializer(serializers.ModelSerializer):
    archivo_pdf = serializers.FileField()

    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'categoria', 'archivo_pdf', 'preguntas','fecha_subida']
    
    def create(self, validated_data):
        preguntas = validated_data.pop('preguntas', [])
        libro = Libro.objects.create(**validated_data)
        libro.preguntas = preguntas
        libro.save()
        return libro
    
    def update(self, instance, validated_data):
        archivo_pdf = validated_data.pop('archivo_pdf', None)

        if archivo_pdf:
            instance.archivo_pdf.delete(save=False)
            instance.archivo_pdf = archivo_pdf
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance