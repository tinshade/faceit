# Generated by Django 3.0.8 on 2021-04-24 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FilezData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.PositiveIntegerField(blank=True, null=True)),
                ('file_owner', models.CharField(max_length=100)),
                ('file_name', models.CharField(max_length=1000)),
                ('file_ext', models.CharField(max_length=90)),
                ('file_size', models.FloatField()),
                ('file_og_location', models.CharField(max_length=2000)),
                ('file_og_checksum', models.CharField(max_length=70)),
                ('file_enc_checksum', models.CharField(max_length=70)),
                ('date_secured', models.CharField(blank=True, max_length=100)),
                ('purge_scheduled', models.BooleanField(default=0)),
                ('enc_level', models.CharField(blank=True, max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
