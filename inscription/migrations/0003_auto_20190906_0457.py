# Generated by Django 2.2.1 on 2019-09-06 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0002_auto_20190905_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscrit',
            name='eleve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscription.Eleve'),
        ),
    ]
