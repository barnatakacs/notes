# Generated by Django 5.0.4 on 2024-08-18 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_tag_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notedata',
            name='tags',
            field=models.ManyToManyField(related_name='notes', to='core.tag'),
        ),
    ]