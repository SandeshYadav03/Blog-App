# Generated by Django 4.0.4 on 2022-04-30 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_postmodel_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='comment_text',
            field=models.TextField(default='Done', max_length=100),
        ),
    ]
