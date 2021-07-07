# Generated by Django 3.2.5 on 2021-07-06 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('handbooks', '0002_auto_20210706_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='HandbookElement',
            fields=[
                ('id', models.CharField(db_index=True, max_length=64, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('code', models.CharField(max_length=15)),
                ('value', models.CharField(max_length=25)),
                ('fk_handbook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handbooks.handbook')),
            ],
        ),
    ]
