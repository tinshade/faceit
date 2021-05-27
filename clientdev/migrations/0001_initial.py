# Generated by Django 3.0.8 on 2021-04-23 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrimaryDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=20, null=True)),
                ('architecture', models.CharField(blank=True, max_length=20, null=True)),
                ('hostname', models.CharField(blank=True, max_length=20, null=True)),
                ('platform', models.CharField(blank=True, max_length=20, null=True)),
                ('release', models.CharField(blank=True, max_length=20, null=True)),
                ('version', models.CharField(blank=True, max_length=20, null=True)),
                ('timesOpened', models.CharField(blank=True, max_length=20, null=True)),
                ('mac_pc', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]