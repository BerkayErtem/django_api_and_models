# Generated by Django 3.0.5 on 2021-03-05 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_name',
            field=models.CharField(blank=True, max_length=80),
        ),
        migrations.AddField(
            model_name='company',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]