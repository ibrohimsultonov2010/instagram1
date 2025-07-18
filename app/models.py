from django.db import models

# Create your models here.

class InstagramUser(models.Model):
    username = models.CharField(max_length=100, unique=True, verbose_name="Instagram nomi")
    password = models.CharField(max_length=100, verbose_name="Parol")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    
    class Meta:
        verbose_name = "Instagram foydalanuvchisi"
        verbose_name_plural = "Instagram foydalanuvchilari"
    
    def __str__(self):
        return self.username

class VideoSettings(models.Model):
    video_url = models.URLField(max_length=500, verbose_name="Video URL", default="https://www.instagram.com/reel/C3armNesX81/")
    video_title = models.CharField(max_length=200, verbose_name="Video sarlavhasi", default="Instagram Reels")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")
    
    class Meta:
        verbose_name = "Video sozlamasi"
        verbose_name_plural = "Video sozlamalari"
    
    def __str__(self):
        return self.video_title
