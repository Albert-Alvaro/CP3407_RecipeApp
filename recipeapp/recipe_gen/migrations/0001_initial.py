# Generated by Django 5.0.2 on 2024-03-19 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ingredient_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_image', models.ImageField(upload_to='../recipeapp/media/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('recipe_content', models.CharField(max_length=5000)),
                ('recipe_steps', models.CharField(max_length=4000)),
                ('recipe_rating', models.IntegerField()),
                ('recipe_category', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('ingredient_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ingredient_name', models.CharField(max_length=60)),
                ('ingredient_type', models.CharField(max_length=60)),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_gen.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_gen.recipe')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_gen.users')),
            ],
        ),
        migrations.CreateModel(
            name='Prompts',
            fields=[
                ('prompt_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('prompt_content', models.CharField(max_length=500)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_gen.users')),
            ],
        ),
    ]