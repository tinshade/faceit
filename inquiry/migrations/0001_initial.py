# Generated by Django 3.0.8 on 2021-04-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=254)),
                ('conact_subject', models.CharField(max_length=100)),
                ('contact_message', models.TextField(max_length=200)),
            ],
        ),
    ]