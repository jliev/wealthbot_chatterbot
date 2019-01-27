# Generated by Django 2.1.4 on 2019-01-12 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ria', '0002_riskquestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('point', models.IntegerField()),
            ],
            options={
                'db_table': 'risk_answers',
            },
        ),
        migrations.AlterField(
            model_name='riskquestion',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='riskquestion',
            name='is_withdraw_age_input',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='riskquestion',
            name='sequence',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='riskquestion',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='riskanswer',
            name='risk_question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ria.RiskQuestion'),
        ),
    ]
