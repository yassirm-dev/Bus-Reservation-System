# Generated by Django 3.1.6 on 2021-07-16 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedseats',
            name='bus',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='buses.bus'),
        ),
    ]
