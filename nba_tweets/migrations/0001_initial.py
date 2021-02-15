# Generated by Django 3.1.5 on 2021-01-25 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.IntegerField()),
                ('screen_name', models.CharField(max_length=100)),
                ('text', models.CharField(max_length=280)),
                ('quote_tweet', models.IntegerField(null=True)),
                ('reply_tweet', models.IntegerField(null=True)),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]
