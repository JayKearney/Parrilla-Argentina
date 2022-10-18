# Generated by Django 3.2.15 on 2022-09-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': ' category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': ' post', 'verbose_name_plural': 'posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/'),
        ),
    ]