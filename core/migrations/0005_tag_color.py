# Generated by Django 5.0.4 on 2024-08-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tag_notedata_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='color',
            field=models.CharField(default='', max_length=100),
        ),
    ]
