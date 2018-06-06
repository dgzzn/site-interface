from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),
    # /music/12
    path('<int:pk>/', views.DetailView.as_view(), name='detalhe'),

    # /music/album/add/
    path('album/add/', views.CriarAlbum.as_view(), name='adicionar-album'),

    # /music/album/2/
    path('album/<int:pk>/', views.UpdateAlbum.as_view(), name='update-album'),

    # /music/album/2/delete/
    path('album/<int:pk>/delete/', views.DeletarAlbum.as_view(), name='deletar-album'),

    # /registrar/
    path('registrar/', views.UserFormView.as_view(), name='registro'),

    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),
    path('login/', auth_views.login, {'template_name': 'music/login.html'}, name='login'),

    path('<int:album_id>/add-musica/', views.create_song, name='add-musica'),
    path('update-musica/', views.UpdateSong.as_view(), name='update-musica'),
    path('<int:album_id>/deletar-musica/<int:musica_id>/', views.delete_song, name='deletar-musica'),
    path('<int:album_id>/favorita/', views.favorita, name='favorita'),
    path('<int:album_id>/favorita-album/', views.favorite_album, name='favorita-album'),
    path('musicas/', views.songs, name='songs'),

    # /login/
    #path('login/', views.LoginView.as_view(), name='login'),

    # logout/
    #path('logout/', views.LogoutView.as_view(), name='logout'),

     #path('login/', login, {'template_name': 'music/login_form.html'}, name='login_user'),



]