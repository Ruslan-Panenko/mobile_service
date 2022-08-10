# Generated by Django 4.1 on 2022-08-09 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_phone_invoice_alter_phone_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.invoice'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='status',
            field=models.CharField(blank=True, choices=[('CD', 'consideration'), ('IP', 'in progress'), ('D', 'done')], max_length=255, null=True),
        ),
    ]
