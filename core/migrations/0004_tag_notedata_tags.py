# Generated by Django 5.0.4 on 2024-08-17 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_notedata_modified_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='notedata',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='notes', to='core.tag'),
        ),
    ]