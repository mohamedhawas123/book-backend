# Generated by Django 4.2.2 on 2023-06-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_page_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
