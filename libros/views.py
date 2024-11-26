from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status

from django.core.mail import send_mail

from .models import Categoria, Libro
from .serializers import CategoriaSerializer, LibroSerializer

class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class LibroListView(generics.ListAPIView):
    serializer_class = LibroSerializer

    def get_queryset(self):
        queryset = Libro.objects.all()
        categoria_id = self.request.query_params.get('categoria', None)
        if categoria_id:
            queryset = queryset.filter(categoria_id=categoria_id)
        return queryset


class LibroUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LibroDetailView(generics.RetrieveAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class EnviarRespuestasView(APIView):
    def post(self, request):
        nombre = request.data.get('nombre')
        respuestas = request.data.get('respuestas')
        libro = request.data.get('libro')

        if not nombre or not respuestas or not libro:
            return Response({"error": "Todos los campos son requeridos."}, status=status.HTTP_400_BAD_REQUEST)

        mensaje = f"Nombre: {nombre}\n\n"
        mensaje += f"Libro: {libro}\n\n"
        for i, respuesta in enumerate(respuestas, 1):
            mensaje += f"Pregunta {i}: {respuesta['pregunta']}\nRespuesta: {respuesta['respuesta']}\n\n"

        try:
            send_mail(
                subject=f"Respuestas del libro {libro}",
                message=mensaje,
                from_email="tu_correo@gmail.com",
                recipient_list=["destinatario@gmail.com"],
            )
            return Response({"message": "Respuestas enviadas correctamente."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": f"Error al enviar el correo: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)