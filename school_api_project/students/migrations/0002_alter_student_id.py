# Generated by Django 3.2.10 on 2024-08-09 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]