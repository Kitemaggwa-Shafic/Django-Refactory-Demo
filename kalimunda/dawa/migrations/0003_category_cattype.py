# Generated by Django 4.1.7 on 2023-03-23 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dawa', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='catType',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
