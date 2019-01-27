# Generated by Django 2.1.4 on 2019-01-08 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20190108_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAdditionalContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('state_id', models.IntegerField(blank=True, default=0, null=True)),
                ('zip', models.CharField(blank=True, max_length=255, null=True)),
                ('is_different_address', models.BooleanField(null=True)),
                ('mailing_street', models.CharField(blank=True, max_length=255, null=True)),
                ('mailing_city', models.CharField(blank=True, max_length=255, null=True)),
                ('mailing_state_id', models.IntegerField(blank=True, default=0, null=True)),
                ('mailing_zip', models.CharField(blank=True, max_length=255, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('dependents', models.SmallIntegerField(blank=True, null=True)),
                ('ssn_tin', models.CharField(blank=True, max_length=20, null=True)),
                ('income_source', models.CharField(blank=True, max_length=100, null=True)),
                ('employer_name', models.CharField(blank=True, max_length=255, null=True)),
                ('industry', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('business_type', models.CharField(blank=True, max_length=255, null=True)),
                ('employer_address', models.CharField(blank=True, max_length=255, null=True)),
                ('employment_city', models.CharField(blank=True, max_length=255, null=True)),
                ('employment_state_id', models.IntegerField(blank=True, default=0, null=True)),
                ('employment_zip', models.CharField(blank=True, max_length=255, null=True)),
                ('is_senior_political_figure', models.BooleanField(null=True)),
                ('senior_spf_name', models.CharField(blank=True, max_length=255, null=True)),
                ('senior_political_title', models.CharField(blank=True, max_length=255, null=True)),
                ('senior_account_owner_relationship', models.CharField(blank=True, max_length=255, null=True)),
                ('senior_country_office', models.CharField(blank=True, max_length=255, null=True)),
                ('is_publicly_traded_company', models.BooleanField(null=True)),
                ('publicle_company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('publicle_address', models.CharField(blank=True, max_length=255, null=True)),
                ('publicle_city', models.CharField(blank=True, max_length=255, null=True)),
                ('publicle_state_id', models.IntegerField(blank=True, default=0, null=True)),
                ('is_broker_security_exchange_person', models.BooleanField(null=True)),
                ('broker_security_exchange_company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('broker_security_exchange_compliance_letter', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(choices=[('spouse', 'spouse'), ('other', 'other')], max_length=10)),
                ('relationship', models.CharField(blank=True, max_length=255, null=True)),
                ('employment_type', models.CharField(blank=True, max_length=50, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=20, null=True)),
                ('spouse_first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('spouse_middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('spouse_last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('spouse_birth_date', models.DateField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'client_additional_contacts',
            },
        ),
        migrations.CreateModel(
            name='ClientSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_tlh_value', models.FloatField(blank=True, null=True)),
                ('client_type', models.CharField(choices=[('new', 'new'), ('current', 'current')], default='new', max_length=10)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'client_settings',
            },
        ),
    ]
