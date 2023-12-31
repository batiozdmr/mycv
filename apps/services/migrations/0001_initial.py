# Generated by Django 4.2.6 on 2023-11-11 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images/')),
                ('content', models.TextField()),
                ('alignment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ServicesSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('content', models.TextField()),
            ],
        ),
    ]
