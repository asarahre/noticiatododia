# Generated by Django 3.2 on 2021-11-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_alter_login_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[['Normal', 'Normal'], ['Administrativo', 'Administrativo']], default='Normal', null=True),
        ),
    ]
