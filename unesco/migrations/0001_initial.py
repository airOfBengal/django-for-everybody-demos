# Generated by Django 3.0.8 on 2020-08-31 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Iso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('year', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=1024)),
                ('justification', models.CharField(max_length=1024)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('area_hectares', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.Category')),
                ('iso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.Iso')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.Region')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unesco.State')),
            ],
        ),
    ]
