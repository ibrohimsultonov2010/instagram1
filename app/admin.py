from django.contrib import admin
from .models import InstagramUser, VideoSettings

# Register your models here.

@admin.register(InstagramUser)
class InstagramUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('username',)
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

@admin.register(VideoSettings)
class VideoSettingsAdmin(admin.ModelAdmin):
    list_display = ('video_title', 'video_url', 'is_active', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('video_title', 'video_url')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-updated_at',)
    
    def has_add_permission(self, request):
        # Faqat bitta video sozlamasi bo'lishi mumkin
        return not VideoSettings.objects.exists()
