# Generated by Django 5.0.6 on 2024-06-26 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannerText', models.TextField()),
                ('bannerImg', models.ImageField(blank=True, default='basic.png', upload_to='')),
            ],
        ),
    ]
