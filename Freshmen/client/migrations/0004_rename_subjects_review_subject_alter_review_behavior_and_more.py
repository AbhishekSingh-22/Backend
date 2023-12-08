# Generated by Django 4.2.7 on 2023-12-01 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_rename_reviews_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='subjects',
            new_name='subject',
        ),
        migrations.AlterField(
            model_name='review',
            name='behavior',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='desc',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='evaluation',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='internals',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='teaching',
            field=models.IntegerField(),
        ),
    ]
