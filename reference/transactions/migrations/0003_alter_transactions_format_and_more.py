# Generated by Django 4.2 on 2023-04-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_alter_transactions_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='format',
            field=models.CharField(choices=[('in-person', 'In-Person'), ('virtual', 'Virtual'), ('phone', 'Phone')], max_length=64),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='location',
            field=models.CharField(choices=[('circ', 'Circulation'), ('ref', 'Reference'), ('childrens', 'Childrens')], max_length=64),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='type',
            field=models.CharField(choices=[('information services', 'Information Services'), ('digital resources', 'Digital Resources'), ('directional', 'Directional'), ('tech help', 'Tech Help')], max_length=64),
        ),
    ]
