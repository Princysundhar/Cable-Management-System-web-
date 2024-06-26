# Generated by Django 3.2.22 on 2024-04-20 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('c_place', models.CharField(max_length=100)),
                ('c_post', models.CharField(max_length=100)),
                ('c_pin', models.CharField(max_length=100)),
                ('c_email', models.CharField(max_length=100)),
                ('c_contact', models.CharField(max_length=100)),
                ('c_photo', models.CharField(max_length=100)),
                ('c_number', models.CharField(max_length=100)),
                ('AREA', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.area')),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('usertype', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pa_type', models.CharField(max_length=100)),
                ('pa_name', models.CharField(max_length=100)),
                ('pa_amount', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='subscription_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('expiry_date', models.CharField(max_length=100)),
                ('CUSTOMER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.customer')),
                ('PACKAGE', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.package')),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('s_place', models.CharField(max_length=100)),
                ('s_post', models.CharField(max_length=100)),
                ('s_pin', models.CharField(max_length=100)),
                ('s_email', models.CharField(max_length=100)),
                ('s_contact', models.CharField(max_length=100)),
                ('s_photo', models.CharField(max_length=100)),
                ('s_qualification', models.CharField(max_length=100)),
                ('s_experience', models.CharField(max_length=100)),
                ('s_category', models.CharField(max_length=100)),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.login')),
            ],
        ),
        migrations.CreateModel(
            name='salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_amount', models.CharField(max_length=100)),
                ('s_credited', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('STAFF', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.staff')),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=1000)),
                ('payment_status', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('month', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('CUSTOMER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.customer')),
            ],
        ),
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_type', models.CharField(max_length=100)),
                ('o_title', models.CharField(max_length=100)),
                ('o_offers', models.CharField(max_length=100)),
                ('STAFF', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.staff')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.login'),
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
                ('reply', models.CharField(max_length=100)),
                ('r_date', models.CharField(max_length=100)),
                ('CUSTOMER', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.customer')),
            ],
        ),
        migrations.CreateModel(
            name='collection_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('p_date', models.CharField(max_length=100)),
                ('p_status', models.CharField(max_length=100)),
                ('SUBSCRIPTION_LIST', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.subscription_list')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_date', models.CharField(max_length=100)),
                ('a_checkin', models.CharField(max_length=100)),
                ('a_checkout', models.CharField(max_length=100)),
                ('STAFF', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.staff')),
            ],
        ),
        migrations.CreateModel(
            name='area_allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AREA', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.area')),
                ('STAFF', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.staff')),
            ],
        ),
    ]
