# Generated by Django 4.0.2 on 2022-02-13 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_noticias_imagem_alter_noticias_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticias',
            name='imagem',
            field=models.ImageField(default='uploads/slide_padrao.png', upload_to='uploads/', verbose_name='Escolha a imagem'),
        ),
    ]
