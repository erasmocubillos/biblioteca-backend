from django.urls import path
from .views import CategoriaListCreateView, LibroListView, LibroUploadView, LibroDetailView, EnviarRespuestasView, create_superuser

urlpatterns = [
    path('categorias/', CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('libros/', LibroListView.as_view(), name='libro-list'),
    path('libros/upload/', LibroUploadView.as_view(), name='libro-upload'),
    path('libros/<int:pk>/', LibroDetailView.as_view(), name='libro-detail'),
    path('enviar-respuestas/', EnviarRespuestasView.as_view(), name='enviar-respuestas'),
    path('create-superuser/', create_superuser),
]
