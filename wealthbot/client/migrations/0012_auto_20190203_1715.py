# Generated by Django 2.1.4 on 2019-02-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_auto_20190203_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='message_code',
            field=models.CharField(choices=[('p10', 'Initial Rebalance'), ('p7', 'New/Update Contributions'), ('p6', 'Banking Information Update'), ('p9', 'Portfolio Proposal'), ('p3', 'Rollover'), ('p2', 'Transfer'), ('p1', 'New Account'), ('p5', 'Address Update'), ('p4', 'New/Update Beneficiary'), ('p8', 'New/Update Distributions'), ('a3', 'Closed Account'), ('a1', 'New Retirement Account')], max_length=3),
        ),
        migrations.AlterModelTable(
            name='activity',
            table='activity',
        ),
    ]
