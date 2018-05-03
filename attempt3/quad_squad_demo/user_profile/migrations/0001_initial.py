# Generated by Django 2.0.4 on 2018-05-02 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'Pending'), ('a', 'Accepted')], help_text='Matches', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textFile', models.FilePathField()),
            ],
        ),
        migrations.CreateModel(
            name='Pending_Meetup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('location', models.CharField(max_length=20)),
                ('time', models.DateTimeField(verbose_name='')),
                ('date', models.DateTimeField(verbose_name='')),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Recommend_Textbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.Degree')),
            ],
        ),
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('pubDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('dob', models.DateTimeField(verbose_name='date of birth')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=300)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.Degree')),
            ],
        ),
        migrations.AddField(
            model_name='recommend_textbook',
            name='textbook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.Textbook'),
        ),
        migrations.AddField(
            model_name='pending_meetup',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guest', to='user_profile.User'),
        ),
        migrations.AddField(
            model_name='pending_meetup',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='host', to='user_profile.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='user_profile.User'),
        ),
        migrations.AddField(
            model_name='message',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='user_profile.User'),
        ),
        migrations.AddField(
            model_name='matches',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='user_profile.User'),
        ),
        migrations.AddField(
            model_name='matches',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='user_profile.User'),
        ),
        migrations.AddField(
            model_name='degree',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile.University'),
        ),
    ]