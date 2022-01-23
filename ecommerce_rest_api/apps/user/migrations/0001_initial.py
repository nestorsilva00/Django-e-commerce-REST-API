# Generated by Django 4.0.1 on 2022-01-11 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=400)),
                ('last_name', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Users',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='User_Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('account_number', models.CharField(max_length=200)),
                ('expiry_date', models.DateField()),
                ('payment_provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.payment_provider')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'verbose_name_plural': 'User Payments',
                'db_table': 'user_payment',
            },
        ),
        migrations.CreateModel(
            name='User_Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('address_line_1', models.CharField(max_length=500)),
                ('address_line_2', models.CharField(max_length=500, null=True)),
                ('city', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('residential_phone_number', models.CharField(max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'verbose_name_plural': 'User Addresses',
                'db_table': 'user_address',
            },
        ),
    ]