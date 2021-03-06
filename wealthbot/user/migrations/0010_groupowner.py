# Generated by Django 2.1.4 on 2019-03-02 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('user', '0009_auto_20190215_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('ria_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'group_owner',
            },
        ),
    ]
