# Generated by Django 5.0 on 2024-01-24 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
