# Generated by Django 2.1.7 on 2024-04-13 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_salary_s_credited'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='STAFF',
        ),
        migrations.AddField(
            model_name='payment',
            name='CUSTOMER',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App.customer'),
            preserve_default=False,
        ),
    ]
