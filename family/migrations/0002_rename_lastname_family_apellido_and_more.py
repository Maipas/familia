# Generated by Django 4.0.4 on 2022-05-29 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='family',
            old_name='lastname',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='family',
            old_name='name',
            new_name='nombre',
        ),
    ]
