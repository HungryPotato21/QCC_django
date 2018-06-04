# Generated by Django 2.0.6 on 2018-06-03 13:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('hits', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
