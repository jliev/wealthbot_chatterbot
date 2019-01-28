# Generated by Django 2.1.4 on 2019-01-28 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webo_admin', '0010_auto_20190126_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecurityTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_fee', models.FloatField(blank=True, null=True)),
                ('transaction_fee_percent', models.FloatField(blank=True, null=True)),
                ('minimum_buy', models.FloatField(blank=True, null=True)),
                ('minimum_initial_buy', models.FloatField(blank=True, null=True)),
                ('minimum_sell', models.FloatField(blank=True, null=True)),
                ('redemption_penalty_interval', models.IntegerField(blank=True, null=True)),
                ('redemption_fee', models.FloatField(blank=True, null=True)),
                ('redemption_percent', models.FloatField(blank=True, null=True)),
                ('security_assignment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='securityTransaction', to='webo_admin.SecurityAssignment')),
            ],
            options={
                'db_table': 'security_transaction',
            },
        ),
    ]