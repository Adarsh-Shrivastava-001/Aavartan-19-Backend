# Generated by Django 2.1.7 on 2019-07-26 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
        ('registration', '0003_auto_20190726_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='events',
            field=models.ManyToManyField(related_name='events', to='Events.Event'),
        ),
    ]
