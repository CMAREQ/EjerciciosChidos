# Generated by Django 2.0 on 2017-12-07 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20)),
                ('Precio', models.PositiveIntegerField()),
                ('Estado', models.BooleanField(default=True)),
            ],
        ),
    ]
