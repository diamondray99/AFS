# Generated by Django 2.2 on 2020-10-25 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201025_2045'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cat_pics/'),
        ),
    ]
