# Generated by Django 5.1.1 on 2024-10-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_coin_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='symbol',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
