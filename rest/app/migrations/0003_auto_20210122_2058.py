# Generated by Django 3.1.5 on 2021-01-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Text',
            field=models.CharField(max_length=1000, verbose_name='Main Text'),
        ),
    ]