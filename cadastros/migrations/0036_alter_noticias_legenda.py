# Generated by Django 4.0.2 on 2022-03-06 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0035_alter_noticias_legenda_alter_noticias_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='legenda',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Legenda (Opcional):'),
        ),
    ]
