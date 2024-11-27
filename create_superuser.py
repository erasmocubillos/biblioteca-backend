from decouple import config

from django.contrib.auth.models import User
from django.db import IntegrityError

USERNAME = config('USERNAME_SUPERUSER')
EMAIL = config('EMAIL_SUPERUSER')
PASSWORD = config('PASSWORD_SUPERUSER')

def run():
    try:
        if not User.objects.filter(username=USERNAME).exists():
            User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
            print("Superusuario creado exitosamente.")
        else:
            print("El superusuario ya existe.")
    except IntegrityError as e:
        print(f"Error al crear el superusuario: {e}")