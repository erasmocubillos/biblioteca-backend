from django.urls import path
from .views import CategoriaListCreateView, LibroListView, LibroUploadView, LibroDetailView, EnviarRespuestasView

urlpatterns = [
    path('categorias/', CategoriaListCreateView.as_view(), name='categoria-list-create'),
    path('categorias/create/', CategoriaListCreateView.as_view(), name='categoria-create'),
    path('libros/', LibroListView.as_view(), name='libro-list'),
    path('libros/upload/', LibroUploadView.as_view(), name='libro-upload'),
    path('libros/<int:pk>/', LibroDetailView.as_view(), name='libro-detail'),
    path('enviar-respuestas/', EnviarRespuestasView.as_view(), name='enviar-respuestas'),
]
