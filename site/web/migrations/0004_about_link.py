# Generated by Django 4.2.5 on 2023-09-30 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_about_img_alter_stat_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='link',
            field=models.CharField(default='qwerty', max_length=100),
        ),
    ]
