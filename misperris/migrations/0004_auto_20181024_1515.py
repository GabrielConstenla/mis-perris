# Generated by Django 2.0.9 on 2018-10-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misperris', '0003_auto_20181023_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoptante',
            name='ciudad',
        ),
        migrations.RemoveField(
            model_name='adoptante',
            name='fechaNacimiento',
        ),
        migrations.RemoveField(
            model_name='adoptante',
            name='region',
        ),
        migrations.RemoveField(
            model_name='adoptante',
            name='vivienda',
        ),
        migrations.AlterField(
            model_name='adoptante',
            name='correo',
            field=models.EmailField(max_length=254),
        ),
    ]
