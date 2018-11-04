# Generated by Django 2.1.3 on 2018-11-04 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenID',
            fields=[
                ('tokenId', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('used', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='candidate',
            name='agendaURL',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='voters',
            name='dateTime',
            field=models.DateTimeField(null=True, verbose_name='date voted'),
        ),
    ]