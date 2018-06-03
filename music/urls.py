from django.urls import path, include
from . import views

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

    path('registrar/', views.UserFormView.as_view(), name='registro')

]