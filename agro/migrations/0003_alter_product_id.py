# Generated by Django 4.2.7 on 2023-11-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agro', '0002_rename_movie_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]