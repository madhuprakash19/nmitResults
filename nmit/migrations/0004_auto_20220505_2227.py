# Generated by Django 3.2.5 on 2022-05-05 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmit', '0003_missing'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpa',
            name='creditsEarn',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='gpa',
            name='creditsReg',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='ay',
            field=models.CharField(blank=True, default='2021-2022', max_length=10, null=True),
        ),
    ]