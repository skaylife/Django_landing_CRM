# Generated by Django 3.1.7 on 2021-03-20 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeleSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tg_token', models.CharField(max_length=200, verbose_name='Токен')),
                ('tg_chat', models.CharField(max_length=200, verbose_name='Id чата')),
                ('tg_message', models.TextField(verbose_name='Текс сообщения')),
            ],
            options={
                'verbose_name': 'Настройку',
                'verbose_name_plural': 'Найстройки',
            },
        ),
    ]
