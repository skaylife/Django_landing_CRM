# Generated by Django 3.1.7 on 2021-03-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsslider',
            name='cms_css',
            field=models.CharField(default='-', max_length=200, null=True, verbose_name='CSS класс'),
        ),
        migrations.AlterField(
            model_name='cmsslider',
            name='cms_img',
            field=models.ImageField(upload_to='slider_img/', verbose_name='Картинка слайда'),
        ),
    ]