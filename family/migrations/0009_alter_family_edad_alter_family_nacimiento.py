# Generated by Django 4.0.4 on 2022-05-30 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0008_alter_family_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='edad',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='family',
            name='nacimiento',
            field=models.FloatField(),
        ),
    ]