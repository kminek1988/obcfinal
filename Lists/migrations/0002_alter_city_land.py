# Generated by Django 3.2.7 on 2021-09-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='land',
            field=models.CharField(choices=[('Bawaria', 'Bawaria'), ('Baden', 'Badenia-Wirtembergia'), ('Hesja', 'Hesja'), ('Brandenburgia', 'Brandenburgia'), ('Brema', 'Brema'), ('Dolna', 'Dolna-Saksonia'), ('Maklemburgia', 'Meklemburgia Pomorze-Przednie'), ('NadreniaPl', 'Nadrenia Północna-Westfalia'), ('Saksonia', 'Saksonia'), ('Nadrenia', 'Nadrenia-Palatynat'), ('Saara', 'Saara'), ('SaksoniaAn', 'Saksonia-Anhalt'), ('Szlezwik', 'Szlezwik-Holsztyn'), ('Turyngia', 'Turyngia')], max_length=255),
        ),
    ]
