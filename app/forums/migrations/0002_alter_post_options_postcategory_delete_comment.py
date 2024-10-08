# Generated by Django 5.0.6 on 2024-06-18 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_posted']},
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forums.post')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
