# Generated by Django 2.1.4 on 2019-02-03 09:22

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_auto_20190203_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='message_code',
            field=models.CharField(choices=[('p5', 'Address Update'), ('p6', 'Banking Information Update'), ('p8', 'New/Update Distributions'), ('p4', 'New/Update Beneficiary'), ('p9', 'Portfolio Proposal'), ('p2', 'Transfer'), ('p7', 'New/Update Contributions'), ('p10', 'Initial Rebalance'), ('p1', 'New Account'), ('p3', 'Rollover'), ('a1', 'New Retirement Account'), ('a3', 'Closed Account')], max_length=3),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_status', models.SmallIntegerField(default=1)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.CharField(default='Prospect Registered', max_length=255)),
                ('is_show_ria', models.BooleanField(default=True)),
                ('client_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clientUserActivities', to='user.User')),
                ('ria_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='riaUserActivities', to='user.User')),
            ],
            options={
                'db_table': 'activity',
            },
        ),
    ]
