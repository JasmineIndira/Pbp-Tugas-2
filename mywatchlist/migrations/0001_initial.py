# Generated by Django 4.1 on 2022-09-21 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyWatchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.BooleanField()),
                ('title', models.CharField(max_length=255)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=5)),
                ('release_date', models.DateField()),
                ('review', models.TextField()),
            ],
        ),
    ]