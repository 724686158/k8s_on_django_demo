# Generated by Django 2.0.3 on 2018-03-13 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreateService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('svc_name', models.CharField(default='my-service', max_length=32)),
                ('svc_protocol', models.CharField(default='TCP', max_length=32)),
                ('svc_spec_selector', models.CharField(max_length=32)),
                ('svc_port', models.CharField(max_length=32)),
                ('svc_target_port', models.CharField(max_length=32)),
            ],
        ),
    ]