# Generated by Django 4.2.5 on 2023-09-30 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='mentors/')),
                ('description_usmle', models.TextField(max_length=255)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
    ]