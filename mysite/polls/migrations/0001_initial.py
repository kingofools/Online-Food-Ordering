# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 12:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('a_id', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('a_name', models.CharField(max_length=200)),
                ('a_mobile', models.DecimalField(decimal_places=0, max_digits=10)),
                ('a_address', models.CharField(max_length=1000)),
                ('a_city', models.CharField(max_length=200)),
                ('a_email', models.EmailField(max_length=200, unique=True)),
                ('a_password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cart_Contains',
            fields=[
                ('cc_id', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='Cart_Item',
            fields=[
                ('cart_item_id', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=3)),
                ('net_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cart_Item_Order',
            fields=[
                ('cio_id', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('cart_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Cart_Item')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('cuisine_id', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('cuisine_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('u_id', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('u_name', models.CharField(max_length=200)),
                ('u_mobile', models.DecimalField(decimal_places=0, max_digits=10)),
                ('u_address', models.CharField(max_length=1000)),
                ('u_city', models.CharField(max_length=200)),
                ('u_email', models.EmailField(max_length=200, unique=True)),
                ('u_password', models.CharField(max_length=200)),
                ('u_latest_cart_id', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('i_id', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
                ('i_name', models.CharField(max_length=200)),
                ('i_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img_url', models.URLField()),
                ('i_cuisine_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Cuisine')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('m_id', models.DecimalField(decimal_places=0, max_digits=5, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Menu_Item',
            fields=[
                ('mi_id', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Item')),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Paid_For',
            fields=[
                ('pf_id', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('cart_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('p_id', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('net_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('r_id', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('r_name', models.CharField(max_length=200)),
                ('r_mobile', models.DecimalField(decimal_places=0, max_digits=10)),
                ('r_address', models.CharField(max_length=1000)),
                ('r_city', models.CharField(max_length=200)),
                ('r_rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('r_email', models.EmailField(max_length=200, unique=True)),
                ('r_password', models.CharField(max_length=200)),
                ('img_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_Menu',
            fields=[
                ('rm_id', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Menu')),
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant_Order',
            fields=[
                ('ro_id', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('cart_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Cart_Item')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Order')),
                ('restaurant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='User_Cart',
            fields=[
                ('uc_id', models.DecimalField(decimal_places=0, max_digits=3, primary_key=True, serialize=False)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Cart')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='pay',
            name='payment_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Payment'),
        ),
        migrations.AddField(
            model_name='paid_for',
            name='payment_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='polls.Payment'),
        ),
        migrations.AddField(
            model_name='cart_item_order',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Order'),
        ),
        migrations.AddField(
            model_name='cart_item',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Item'),
        ),
        migrations.AddField(
            model_name='cart_item',
            name='restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Restaurant'),
        ),
        migrations.AddField(
            model_name='cart_contains',
            name='cart_item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Cart_Item'),
        ),
    ]
