#views 3

from django.http import FileResponse
from django.shortcuts import render
from pytube import YouTube
import os

def index(request):
    if request.method == 'POST':
        video_url = request.POST['video_url']
        try:
            yt = YouTube(video_url)
            video = yt.streams.filter(file_extension='mp4', progressive=True).first()
            video_path = f'media/{yt.title}.mp4'
            video.download('media/', filename=yt.title)
            
            response = FileResponse(open(video_path, 'rb'), as_attachment=True)
            response['Content-Disposition'] = f'attachment; filename="{yt.title}.mp4"'
            return response
        except Exception as e:
            context = {'error': True, 'error_message': str(e)}
    else:
        context = {}
    return render(request, 'downloader/index.html', context)
