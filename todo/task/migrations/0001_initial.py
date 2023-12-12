# Generated by Django 4.1.1 on 2022-09-11 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('task_content', models.TextField()),
                ('created_date', models.DateTimeField()),
            ],
        ),
    ]
