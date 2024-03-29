# Generated by Django 4.2.1 on 2024-02-19 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_create'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-fixed', '-create'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AddField(
            model_name='post',
            name='fixed',
            field=models.BooleanField(default=False, verbose_name='Прикреплено'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-fixed', '-create', 'status'], name='blog_post_fixed_0994c8_idx'),
        ),
    ]
