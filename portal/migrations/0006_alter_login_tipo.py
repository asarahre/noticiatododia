# Generated by Django 3.2 on 2021-11-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_alter_login_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='tipo',
            field=models.CharField(choices=[('ADM', 'Adm'), ('NOR', 'Normal')], default='NOR', max_length=50),
        ),
    ]
