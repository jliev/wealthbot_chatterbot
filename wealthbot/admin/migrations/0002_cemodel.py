# Generated by Django 2.1.4 on 2019-01-24 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_user_appointedbillingspec'),
        ('webo_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('is_deleted', models.BooleanField()),
                ('risk_rating', models.IntegerField(null=True)),
                ('commission_min', models.FloatField(null=True)),
                ('commission_max', models.FloatField(null=True)),
                ('forecast', models.IntegerField(null=True)),
                ('generous_market_return', models.FloatField(null=True)),
                ('low_market_return', models.FloatField(null=True)),
                ('is_assumption_locked', models.BooleanField()),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webo_admin.CeModel')),
            ],
            options={
                'db_table': 'ce_models',
            },
        ),
    ]
