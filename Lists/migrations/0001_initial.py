# Generated by Django 3.2.7 on 2021-09-27 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='nazwa')),
                ('letter', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('R', 'R'), ('S', 'S'), ('T', 'T'), ('U', 'U'), ('W', 'W'), ('V', 'V'), ('Z', 'Z'), ('Ö', 'Ö'), ('Ä', 'Ä'), ('Ü', 'Ü')], max_length=1, verbose_name='litera')),
                ('land', models.CharField(choices=[('Baden', 'Baden-Wurtenberg'), ('Saksonia', 'Saksonia')], max_length=255)),
            ],
            options={
                'verbose_name': 'Miasto',
                'verbose_name_plural': 'Miasta',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='nazwa')),
                ('opis', models.TextField(blank=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Lists.city', verbose_name='miasto')),
            ],
            options={
                'verbose_name': 'Kategoria',
                'verbose_name_plural': 'Kategorie',
            },
        ),
    ]
