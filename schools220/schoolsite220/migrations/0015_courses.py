# Generated by Django 3.2.12 on 2022-04-06 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolsite220', '0014_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=100, null=True)),
                ('fullname', models.CharField(blank=True, max_length=100, null=True)),
                ('short_description', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField()),
                ('day', models.CharField(max_length=19)),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
            },
        ),
    ]