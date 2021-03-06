# Generated by Django 3.0.8 on 2020-08-31 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='iso',
            name='name',
            field=models.CharField(max_length=2, unique=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='area_hectares',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
