# Generated by Django 3.1.3 on 2021-04-16 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TransactionName', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Accounts API Transaction',
                'verbose_name_plural': 'Accounts API Transactions',
            },
        ),
        migrations.CreateModel(
            name='TransactionParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ParameterName', models.CharField(max_length=100)),
                ('ParameterValue', models.CharField(blank=True, max_length=250, null=True)),
                ('TransactionName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='oach_accounts_api.transaction')),
            ],
            options={
                'verbose_name': 'Accounts API Parameter',
                'verbose_name_plural': 'Accounts API Parameters',
            },
        ),
        migrations.AddConstraint(
            model_name='transaction',
            constraint=models.UniqueConstraint(fields=('TransactionName',), name='unique accountstransactionname'),
        ),
        migrations.AddConstraint(
            model_name='transactionparameter',
            constraint=models.UniqueConstraint(fields=('TransactionName', 'ParameterName'), name='unique accountstransactionparameter'),
        ),
    ]
