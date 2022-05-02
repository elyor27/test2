# Generated by Django 3.2 on 2021-05-03 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='brand',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.brandmodel'),
            preserve_default=False,
        ),
    ]