# Generated by Django 2.2.1 on 2019-09-04 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscrit',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='inscrit',
            name='eleve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscription.Eleve', unique=True),
        ),
    ]
