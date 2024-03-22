# Generated by Django 5.0.2 on 2024-03-22 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_gen', '0004_result_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='ingredient_name',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='ingredients',
            name='ingredient_type',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.DeleteModel(
            name='result_images',
        ),
    ]