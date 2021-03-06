# Generated by Django 2.2.6 on 2019-10-26 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('small_size_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('med_size_price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaFlavor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flavor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pizza_app.Flavor')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pizza_app.Pizza')),
            ],
        ),
        migrations.AddField(
            model_name='flavor',
            name='on_top_of',
            field=models.ManyToManyField(through='pizza_app.PizzaFlavor', to='pizza_app.Pizza'),
        ),
    ]
