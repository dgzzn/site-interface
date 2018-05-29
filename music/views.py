from django.shortcuts import render, get_object_or_404
from .models import Album, Musica
from django.views import generic


"""
def index(request):
    todos_albums = Album.objects.all()
    return render(request, 'music/music.html', {'todos_albums': todos_albums})


def detalhe(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detalhe.html',{'album': album})

"""

class IndexView(generic.ListView):
    template_name = 'music/music.html'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detalhe.html'











