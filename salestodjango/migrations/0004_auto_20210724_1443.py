# Generated by Django 3.2.5 on 2021-07-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salestodjango', '0003_account_contact_sfusers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sfusers',
            name='LastLoginDate',
        ),
        migrations.AlterField(
            model_name='account',
            name='LastActivityDate',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
