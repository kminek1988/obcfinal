# Generated by Django 3.2.7 on 2021-10-04 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_profil_black'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='black',
            field=models.BooleanField(default=False),
        ),
    ]
