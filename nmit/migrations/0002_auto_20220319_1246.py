# Generated by Django 3.2.5 on 2022-03-19 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpa',
            name='cgpa',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='gpa',
            name='sgpa',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
