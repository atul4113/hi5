# Generated by Django 2.0.7 on 2018-08-19 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scrap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=2000)),
                ('phone', models.CharField(max_length=20)),
                ('img_path', models.CharField(max_length=2000)),
            ],
        ),
        migrations.RemoveField(
            model_name='data',
            name='address',
        ),
        migrations.RemoveField(
            model_name='data',
            name='img_path',
        ),
        migrations.RemoveField(
            model_name='data',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='data',
            name='store_name',
        ),
    ]
