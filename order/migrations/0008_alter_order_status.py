# Generated by Django 4.2.4 on 2023-09-23 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_productinbasket_options_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.status'),
        ),
    ]
