# Generated by Django 3.2.13 on 2022-06-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20220614_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='college_profile_pic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_path', models.CharField(max_length=100)),
            ],
        ),
    ]
