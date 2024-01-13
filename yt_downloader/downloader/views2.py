from django.http import FileResponse
from django.utils.encoding import smart_str
from django.shortcuts import render
from pytube import YouTube

def index(request):
    if request.method == 'POST':
        video_url = request.POST['video_url']
        try:
            yt = YouTube(video_url)
            video = yt.streams.filter(file_extension='mp4', progressive=True).first()
            video_path = f'media/{smart_str(yt.title)}.mp4'
            video.download('media/', filename=smart_str(yt.title))
            response = FileResponse(open(video_path, 'rb'))
            response['Content-Disposition'] = f'attachment; filename="{yt.title}.mp4"'
            return response
        except Exception as e:
            context = {'error': True, 'error_message': str(e)}
    else:
        context = {}
    return render(request, 'downloader/index.html', context)
