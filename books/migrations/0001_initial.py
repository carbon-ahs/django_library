# Generated by Django 4.0 on 2023-12-05 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=50, verbose_name='Subtitle')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
                ('isbn', models.CharField(max_length=13, verbose_name='ISBN')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
