# Generated by Django 3.1.5 on 2021-03-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210205_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='sno',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]