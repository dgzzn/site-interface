from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Musica
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import View
from .models import Album
from .forms import UserForm, UserLoginForm , MusicaForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.http import is_safe_url




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
    # template_name = 'music/album_form.html'
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
        return render(request, self.template_name, {'form': form})

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


class LoginView(View):
    sucess_url = reverse_lazy('music:index')
    form_class = AuthenticationForm
    template_name = 'music/login_form.html'


class LoginView(FormView):
    success_url = reverse_lazy('music:index')
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'music/login_form.html'

    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        if self.request.session.test.cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.GET.get(self, 'music/login_form.html')
        if not is_safe_url(url=redirect_to, host=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to


class LogoutView(RedirectView):
    url = 'music/music.html'

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class ListSong(generic.ListView):

    template_name = 'music/detalhe2.html'

    def get_queryset(self):
        return Musica.objects.all()


class CreateSong(CreateView):

    model = Musica
    fields = ['nome', 'favorita', 'arquivo_musica']

    def form_valid(self, form):

        form.instance.album = self.request.POST
        return super(CreateSong, self).form_valid(form)




"""
    def get(self, request):
        form = MusicaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = MusicaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.Album = request.Album
            post.save()
            dados = form.cleaned_data['post']
            form = MusicaForm()
            return redirect('musica:detalhe')

        args = {'form': form}
        return render(request, self.template_name, args)
"""



class UpdateSong(UpdateView):
    model = Musica
    fields = ['nome', 'favorita', 'arquivo_musica']


class DeleteSong(DeleteView):
    model = Musica

    def get_success_url(self):
        album = self.object.album
        musica = self.object.musica

        return reverse_lazy('music:detalhe2', kwargs={'album': album})


def delete_song(request, album_id, musica_id):
    album = get_object_or_404(Album, pk=album_id)
    musica = Musica.objects.get(pk=musica_id)
    musica.delete()
    return render(request, 'music/detalhe2.html', {'album': album})



"""
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'albums': albums})
            else:
                return render(request, 'music/login_form.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login_form.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login_form.html')


"""


def create_song(request, album_id):
    form = MusicaForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Album, pk=album_id)
    if form.is_valid():
        albums_songs = album.musica_set.all()
        for s in albums_songs:
            if s.nome == form.cleaned_data.get("nome"):
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'music/musica_form.html', context)
        musica = form.save(commit=False)
        musica.album = album
        musica.arquivo_musica = request.FILES['arquivo_musica']
        file_type = musica.arquivo_musica.url.split('.')[-1]
        file_type = file_type.lower()

        context = {
            'album': album,
            'form': form,
        }

        musica.save()
        return render(request, 'music/detalhe2.html', context)
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'music/musica_form.html', context)


def delete_song(request, album_id, musica_id):
    album = get_object_or_404(Album, pk=album_id)
    musica = Musica.objects.get(pk=musica_id)
    musica.delete()
    return render(request, 'music/detalhe2.html', {'album': album})


def favorita(request, musica_id):
    musica = get_object_or_404(Musica, pk=musica_id)
    try:
        if musica.favorita:
            musica.favorita = False
        else:
            musica.favorita = True
        musica.save()
    except (KeyError, Musica.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def favorite_album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        if album.favorito:
            album.favorito = False
        else:
            album.favorito = True
        album.save()
    except (KeyError, Album.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})

def songs(request):
        try:
            musica_ids = []
            for album in Album.objects.filter(user=request.user):
                for musica in album.musica_set.all():
                    musica_ids.append(musica.pk)
            users_songs = Musica.objects.filter(pk__in=musica_ids)

        except Album.DoesNotExist:
            users_songs = []
        return render(request, 'music/songs.html', {
            'song_list': users_songs

})