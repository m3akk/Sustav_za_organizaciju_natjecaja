# Generated by Django 4.1.7 on 2023-03-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_datum_natjecaj_natjecaj_datum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prijava',
            name='prijava_broj',
            field=models.IntegerField(),
        ),
    ]
