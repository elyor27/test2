# Generated by Django 3.2 on 2021-05-19 12:48

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_authormodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authormodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='authormodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='authors', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='authormodel',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='posts.authormodel', verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='banner',
            field=models.ImageField(upload_to='banners', verbose_name='banner'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(upload_to='posts', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='posts.PostTagModel', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(max_length=512, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='posttagmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='posttagmodel',
            name='title',
            field=models.CharField(max_length=20, verbose_name='title'),
        ),
    ]
