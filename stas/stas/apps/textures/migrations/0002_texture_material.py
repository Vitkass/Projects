# Generated by Django 3.0.3 on 2020-09-23 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='texture',
            name='material',
            field=models.CharField(default='Фотофон', max_length=50, verbose_name='Изделие'),
            preserve_default=False,
        ),
    ]
