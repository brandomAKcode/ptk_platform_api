# Generated by Django 5.0.6 on 2024-06-05 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userPTK', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userptk',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
