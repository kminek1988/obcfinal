# Generated by Django 3.2.7 on 2021-10-02 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, unique=True, verbose_name='pseudonim')),
                ('imie', models.CharField(blank=True, max_length=255, null=True, verbose_name='imię')),
                ('nazwisko', models.CharField(blank=True, max_length=255, null=True, verbose_name='nazwisko')),
                ('miasto', models.CharField(blank=True, max_length=255, null=True, verbose_name='miasto')),
                ('profesja', models.CharField(blank=True, max_length=255, null=True, verbose_name='profesja')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'kontakt',
                'verbose_name_plural': 'kontakty',
            },
        ),
    ]
