from django.urls import path
from .views import CategoriaListCreateView, LibroListView, LibroUploadView, LibroDetailView, EnviarRespuestasView

from django.contrib.auth.models import User
from django.http import JsonResponse

def create_superuser(request):
    if User.objects.filter(is_superuser=True).exists():
        return JsonResponse({"error": "El superusuario ya existe"}, status=400)

    # Crea el superusuario
    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="admin123"
    )
    return JsonResponse({"success": "Superusuario creado exitosamente"})

urlpatterns = [
    path('categorias/', CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('libros/', LibroListView.as_view(), name='libro-list'),
    path('libros/upload/', LibroUploadView.as_view(), name='libro-upload'),
    path('libros/<int:pk>/', LibroDetailView.as_view(), name='libro-detail'),
    path('enviar-respuestas/', EnviarRespuestasView.as_view(), name='enviar-respuestas'),
    path('create-superuser/', create_superuser),
]
