# Generated by Django 2.2 on 2018-11-05 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokenNo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TokenDash',
            fields=[
            ],
            options={
                'verbose_name': 'Token Dashboard',
                'verbose_name_plural': 'Token Dashboard',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('polls.tokenno',),
        ),
    ]