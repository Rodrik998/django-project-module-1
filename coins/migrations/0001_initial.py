# Generated by Django 4.1.7 on 2023-03-19 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=5)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='coins')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('amount', models.FloatField()),
                ('date', models.DateField()),
                ('transaction_type', models.CharField(choices=[('buy', 'buy'), ('sell', 'sell')], max_length=4)),
                ('coins', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='coins.coin')),
            ],
        ),
    ]
