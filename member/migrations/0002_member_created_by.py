# Generated by Django 4.2.3 on 2023-07-30 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='created_by',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]