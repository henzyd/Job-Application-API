# Generated by Django 4.1.2 on 2022-10-24 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobAdvert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=150)),
                ('employment_type', models.CharField(choices=[('FULL_TIME', 'Full-time'), ('CONTRACT', 'Contract'), ('REMOTE', 'Remote'), ('PART_TIME', 'Part-time')], max_length=30)),
            ],
        ),
    ]
