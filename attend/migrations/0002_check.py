# Generated by Django 2.1.7 on 2019-03-31 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('checking', models.IntegerField()),
            ],
        ),
    ]
