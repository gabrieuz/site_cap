# Generated by Django 4.0.2 on 2022-02-14 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0009_alter_noticias_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='imagem',
            field=models.ImageField(default='/foto_padrao.png', upload_to='fotos', verbose_name='Escolha a imagem:'),
        ),
        migrations.AlterField(
            model_name='noticias',
            name='imagem',
            field=models.ImageField(default='/slide_padrao.png', upload_to='slides', verbose_name='Escolha a imagem:'),
        ),
    ]
