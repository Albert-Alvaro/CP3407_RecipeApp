# Generated by Django 5.0.2 on 2024-03-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_gen', '0002_alter_ingredient_images_ingredient_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient_images',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]