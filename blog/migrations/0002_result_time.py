# Generated by Django 4.2.5 on 2023-10-03 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]