from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse, Http404
from rest_framework.authtoken.views import obtain_auth_token
import os

def root_view(request):
    return HttpResponse("Bienvenido a la API de Biblioteca Digital")


def serve_pdf(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if not os.path.exists(file_path):
        raise Http404("El archivo solicitado no existe.")

    with open(file_path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response

urlpatterns = [
    path('', root_view),
    path('admin/', admin.site.urls),
    path('api/', include('libros.urls')),
    path('api/token/', obtain_auth_token, name='obtain-token'),
    path('media/<path:path>', serve_pdf),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)