# Generated by Django 3.2.7 on 2021-10-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_alter_profil_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='typ',
            field=models.CharField(choices=[('Szukający', 'Szukający'), ('Obrotny', 'Obrotny')], max_length=255, null=True),
        ),
    ]