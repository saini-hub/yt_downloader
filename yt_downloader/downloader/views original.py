#views original
from django.shortcuts import render
from pytube import YouTube

def index(request):
    if request.method == 'POST':
        video_url = request.POST['video_url']
        try:
            yt = YouTube(video_url)
            video = yt.streams.filter(file_extension='mp4', progressive=True).first()
            video.download('media/')
            context = {'success': True, 'title': yt.title}
        except Exception as e:
            context = {'error': True, 'error_message': str(e)}
    else:
        context = {}
    return render(request, 'downloader/index.html', context)
