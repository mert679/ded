# Generated by Django 4.0 on 2022-02-15 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='temperature',
            field=models.CharField(max_length=100),
        ),
    ]
