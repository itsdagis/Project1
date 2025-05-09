# Generated by Django 5.2 on 2025-04-23 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Category_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Category_Name', models.CharField(max_length=100, unique=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Created_At', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Order_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Order_Date', models.DateTimeField(auto_now_add=True)),
                ('Total_Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Age', models.IntegerField()),
                ('Phone', models.CharField(max_length=50)),
                ('Joined_At', models.DateTimeField(auto_now_add=True)),
                ('Note', models.TextField()),
                ('IsActive', models.BooleanField()),
                ('Exact_Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('Payment_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Payment_Date', models.DateTimeField(auto_now_add=True)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('Credit Card', 'Credit Card'), ('Paypal', 'Paypal'), ('Bank Transfer', 'Bank Transfer')], max_length=20)),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Payments', to='usersite.order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Product_Name', models.CharField(max_length=100)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Stock', models.IntegerField(default=0)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Products', to='usersite.category')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Products', to='usersite.product'),
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('Shipping_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Shipping_Address', models.CharField(max_length=255)),
                ('Shipping_Date', models.DateTimeField(blank=True, null=True)),
                ('Delivery_Date', models.DateTimeField(blank=True, null=True)),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Shippings', to='usersite.order')),
            ],
        ),
        migrations.CreateModel(
            name='Shopping_Cart',
            fields=[
                ('Cart_Id', models.AutoField(primary_key=True, serialize=False)),
                ('Created_At', models.DateTimeField(auto_now_add=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Shopping_Carts', to='usersite.user')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Orders', to='usersite.user'),
        ),
    ]
