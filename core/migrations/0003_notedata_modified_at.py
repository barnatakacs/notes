# Generated by Django 5.0.4 on 2024-08-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_notedata_delete_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='notedata',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
