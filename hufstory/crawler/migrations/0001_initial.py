# Generated by Django 2.0.7 on 2019-05-06 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('major', models.CharField(max_length=50)),
                ('post_num', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('url', models.TextField()),
            ],
        ),
    ]