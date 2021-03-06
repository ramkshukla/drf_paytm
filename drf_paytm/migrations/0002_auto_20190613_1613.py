# Generated by Django 2.2.2 on 2019-06-13 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf_paytm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paytmconfiguration',
            name='base_url',
            field=models.URLField(default='http://127.0.0.1:8000', verbose_name='Base URL (without / at end)'),
        ),
        migrations.AlterField(
            model_name='transactionrequest',
            name='channel',
            field=models.CharField(choices=[('WEB', 'Website'), ('WAP', 'Mobile Website/App')], default='WEB', max_length=3, verbose_name='Channel'),
        ),
        migrations.AlterField(
            model_name='transactionrequest',
            name='itid',
            field=models.CharField(default='Retail', max_length=20, verbose_name='Industry Type ID'),
        ),
        migrations.AlterField(
            model_name='transactionrequest',
            name='website',
            field=models.CharField(default='WEBSTAGING', max_length=30, verbose_name='Website'),
        ),
    ]
