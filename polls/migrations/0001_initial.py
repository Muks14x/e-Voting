# Generated by Django 2.1.3 on 2018-11-05 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucketName', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=1)),
                ('hostel', models.CharField(choices=[('BH1', 'Boys-Hostel1'), ('GH1', 'Girls-Hostel1')], max_length=3)),
                ('year', models.IntegerField(choices=[(0, 'All'), (15, '15'), (16, '16'), (17, '17'), (18, '18')])),
                ('course', models.CharField(choices=[('B', 'BTech'), ('M', 'MTech'), ('P', 'Phd')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('name', models.CharField(default='', max_length=200)),
                ('agendaURL', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('posID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('posName', models.CharField(max_length=200)),
                ('buckets', models.ManyToManyField(to='polls.Bucket')),
            ],
            options={
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='TokenID',
            fields=[
                ('tokenID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('used', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TokenNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokenNo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Voters',
            fields=[
                ('voterID', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('hasVoted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Votes1',
            fields=[
                ('tokenID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('voteJSON', models.CharField(max_length=1000)),
                ('signature', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Positions'),
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
            },
            bases=('polls.tokenno',),
        ),
    ]
