# Generated by Django 4.0.2 on 2022-02-23 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0017_fotos_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='categoria',
            field=models.CharField(choices=[('FUND_I', 'Fundamental I'), ('FUND_II', 'Fundamental II'), ('MEDIO', 'Médio')], default='FUND_I', max_length=20),
        ),
    ]