# Generated by Django 4.2.7 on 2023-12-01 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('subjects', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
                ('teaching', models.CharField(max_length=20)),
                ('evaluation', models.CharField(max_length=20)),
                ('behavior', models.CharField(max_length=20)),
                ('internals', models.CharField(max_length=20)),
                ('class_average_marks', models.CharField(max_length=20)),
                ('overall', models.CharField(max_length=20)),
            ],
        ),
    ]