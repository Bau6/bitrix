# Generated by Django 5.0.7 on 2024-07-25 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=10)),
                ('path', models.CharField(max_length=200)),
                ('user_agent', models.CharField(blank=True, max_length=255, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=39, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('response_status', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
