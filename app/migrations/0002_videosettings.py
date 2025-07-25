# Generated by Django 5.2.2 on 2025-07-18 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.URLField(default='https://www.instagram.com/reel/C3armNesX81/', max_length=500, verbose_name='Video URL')),
                ('video_title', models.CharField(default='Instagram Reels', max_length=200, verbose_name='Video sarlavhasi')),
                ('is_active', models.BooleanField(default=True, verbose_name='Faol')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan vaqti')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan vaqti')),
            ],
            options={
                'verbose_name': 'Video sozlamasi',
                'verbose_name_plural': 'Video sozlamalari',
            },
        ),
    ]
