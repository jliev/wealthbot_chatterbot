# Generated by Django 2.1.4 on 2019-01-26 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webo_admin', '0008_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fee',
            old_name='billingSpec',
            new_name='billing_spec',
        ),
    ]
