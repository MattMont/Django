# Generated by Django 2.0.5 on 2018-06-25 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homevalue', '0002_auto_20180625_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeinfo',
            name='city',
            field=models.CharField(default='Edmonton', max_length=50),
        ),
        migrations.AddField(
            model_name='homeinfo',
            name='country',
            field=models.CharField(default='Canada', max_length=100),
        ),
        migrations.AddField(
            model_name='homeinfo',
            name='province',
            field=models.CharField(default='Alberta', max_length=30),
        ),
        migrations.AlterField(
            model_name='homeinfo',
            name='address',
            field=models.CharField(max_length=150),
        ),
    ]