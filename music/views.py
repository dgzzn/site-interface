from django.shortcuts import render, redirect
from .models import Album, Musica
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Album
from .forms import UserForm



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
    template_name = 'music/detalhe2.html'


class CriarAlbum(CreateView):
    model = Album
    # template_name = 'music/album_form.html'
    fields = ['artista', 'titulo', 'genero', 'capa', 'ano']


class UpdateAlbum(UpdateView):
    model = Album
    #template_name = 'music/album_form.html'
    fields = ['artista', 'titulo', 'genero', 'capa', 'ano']


class DeletarAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registro_form.html'

    # mostra formulário em branco
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # processa os dados do formulário
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # dados padronizados
            username = form.cleaned_data['username']
            senha = form.cleaned_data['senha']
            user.set_password(senha)
            user.save()

            # retorna User objects se credenciais estiverem corretas
            user = authenticate(username=username, password=senha)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})




