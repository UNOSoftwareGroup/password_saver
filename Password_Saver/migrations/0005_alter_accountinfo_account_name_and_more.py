# Generated by Django 4.1.5 on 2023-04-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Password_Saver', '0004_alter_accountinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountinfo',
            name='account_name',
            field=models.CharField(max_length=200, verbose_name='Account Name '),
        ),
        migrations.AlterField(
            model_name='accountinfo',
            name='password',
            field=models.CharField(max_length=200, verbose_name='Password '),
        ),
        migrations.AlterField(
            model_name='accountinfo',
            name='user_name',
            field=models.CharField(max_length=200, verbose_name='User Name '),
        ),
    ]
