# Generated by Django 3.2.5 on 2022-03-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nmit', '0002_auto_20220319_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='missing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usn', models.CharField(blank=True, max_length=10, null=True)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
