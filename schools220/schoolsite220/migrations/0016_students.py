# Generated by Django 3.2.12 on 2022-04-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolsite220', '0015_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('fullname', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='students')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
            },
        ),
    ]