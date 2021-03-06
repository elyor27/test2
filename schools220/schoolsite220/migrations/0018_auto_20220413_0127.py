# Generated by Django 3.2.12 on 2022-04-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolsite220', '0017_auto_20220411_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutschool',
            name='describtions_en',
            field=models.TextField(null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='aboutschool',
            name='describtions_ru',
            field=models.TextField(null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='aboutschool',
            name='describtions_uz',
            field=models.TextField(null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='aboutschool',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='aboutschool',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='aboutschool',
            name='title_uz',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='banner',
            name='descriptions_en',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='banner',
            name='descriptions_ru',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='banner',
            name='descriptions_uz',
            field=models.CharField(blank=True, max_length=2000, null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title_en',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title_ru',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='banner',
            name='title_uz',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_name_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='course_name'),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_name_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='course_name'),
        ),
        migrations.AddField(
            model_name='courses',
            name='course_name_uz',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='course_name'),
        ),
        migrations.AddField(
            model_name='courses',
            name='description_en',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='courses',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='courses',
            name='description_uz',
            field=models.TextField(null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='courses',
            name='short_description_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='short_description'),
        ),
        migrations.AddField(
            model_name='courses',
            name='short_description_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='short_description'),
        ),
        migrations.AddField(
            model_name='courses',
            name='short_description_uz',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='short_description'),
        ),
        migrations.AddField(
            model_name='features',
            name='descriptions_en',
            field=models.TextField(null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='features',
            name='descriptions_ru',
            field=models.TextField(null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='features',
            name='descriptions_uz',
            field=models.TextField(null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='features',
            name='title_en',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='features',
            name='title_ru',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='features',
            name='title_uz',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='managements',
            name='biografy_en',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='biografy'),
        ),
        migrations.AddField(
            model_name='managements',
            name='biografy_ru',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='biografy'),
        ),
        migrations.AddField(
            model_name='managements',
            name='biografy_uz',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='biografy'),
        ),
        migrations.AddField(
            model_name='managements',
            name='fullname_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='fullname'),
        ),
        migrations.AddField(
            model_name='managements',
            name='fullname_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='fullname'),
        ),
        migrations.AddField(
            model_name='managements',
            name='fullname_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='fullname'),
        ),
        migrations.AddField(
            model_name='managements',
            name='pozitions_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='pozitions'),
        ),
        migrations.AddField(
            model_name='managements',
            name='pozitions_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='pozitions'),
        ),
        migrations.AddField(
            model_name='managements',
            name='pozitions_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='pozitions'),
        ),
        migrations.AddField(
            model_name='news',
            name='descriptions_en',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='news',
            name='descriptions_ru',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='news',
            name='descriptions_uz',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='descriptions'),
        ),
        migrations.AddField(
            model_name='news',
            name='short_descriptions_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='short_descriptions'),
        ),
        migrations.AddField(
            model_name='news',
            name='short_descriptions_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='short_descriptions'),
        ),
        migrations.AddField(
            model_name='news',
            name='short_descriptions_uz',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='short_descriptions'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_uz',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='staff',
            name='biografy_en',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='biografy'),
        ),
        migrations.AddField(
            model_name='staff',
            name='biografy_ru',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='biografy'),
        ),
        migrations.AddField(
            model_name='staff',
            name='biografy_uz',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='biografy'),
        ),
        migrations.AddField(
            model_name='staff',
            name='fullname_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='fullname'),
        ),
        migrations.AddField(
            model_name='staff',
            name='fullname_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='fullname'),
        ),
        migrations.AddField(
            model_name='staff',
            name='fullname_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='fullname'),
        ),
        migrations.AddField(
            model_name='staff',
            name='pozitions_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='pozitions'),
        ),
        migrations.AddField(
            model_name='staff',
            name='pozitions_ru',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='pozitions'),
        ),
        migrations.AddField(
            model_name='staff',
            name='pozitions_uz',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='pozitions'),
        ),
        migrations.AddField(
            model_name='students',
            name='content_en',
            field=models.TextField(null=True, verbose_name='contact'),
        ),
        migrations.AddField(
            model_name='students',
            name='content_ru',
            field=models.TextField(null=True, verbose_name='contact'),
        ),
        migrations.AddField(
            model_name='students',
            name='content_uz',
            field=models.TextField(null=True, verbose_name='contact'),
        ),
        migrations.AddField(
            model_name='students',
            name='fullname_en',
            field=models.CharField(max_length=50, null=True, verbose_name='fullname'),
        ),
        migrations.AddField(
            model_name='students',
            name='fullname_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='fullname'),
        ),
        migrations.AddField(
            model_name='students',
            name='fullname_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='fullname'),
        ),
        migrations.AddField(
            model_name='students',
            name='title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='students',
            name='title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='students',
            name='title_uz',
            field=models.CharField(max_length=50, null=True, verbose_name='title'),
        ),
    ]
