# Generated by Django 5.1.3 on 2024-11-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='archivo_pdf',
            field=models.FileField(upload_to='libros/'),
        ),
    ]
