# Generated by Django 2.2.6 on 2019-10-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_order_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Processing'), (2, 'On the way'), (3, 'Delivered')], default=1),
        ),
    ]
