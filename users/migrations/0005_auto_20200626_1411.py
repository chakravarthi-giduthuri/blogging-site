# Generated by Django 3.0.5 on 2020-06-26 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200626_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]