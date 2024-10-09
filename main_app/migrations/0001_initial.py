# Generated by Django 5.1.1 on 2024-10-09 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
                ('price', models.FloatField()),
                ('market_cap', models.FloatField()),
                ('volume', models.FloatField()),
                ('change', models.FloatField()),
                ('image', models.URLField()),
            ],
        ),
    ]
