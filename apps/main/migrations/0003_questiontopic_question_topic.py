# Generated by Django 4.2.6 on 2023-10-28 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.questiontopic'),
        ),
    ]
