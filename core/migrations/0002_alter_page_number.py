# Generated by Django 4.2.2 on 2023-06-21 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
