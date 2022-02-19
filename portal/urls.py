from django.urls import path
from . import views

urlpatterns = [
    path('editar_noticia/<int:noticia_pk>', views.editar_noticia, name='editar_noticia'),
    path('editauser/<int:login_pk>', views.editauser, name='editauser'),

    path('', views.home, name='home'),
    path('noticia/', views.noticia, name='noticia'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('excluirnoticia/', views.excluirnoticia, name='excluirnoticia'),
    path('adicionarnoticia/', views.adicionarnoticia, name='adicionarnoticia'),
    path('modificarnoticia/', views.modificarnoticia, name='modificarnoticia'),
    path('excluircomentario/', views.excluircomentario, name='excluircomentario'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('usuario/', views.usuario, name='usuario'),
    path('sobrenos/', views.sobrenos, name='sobrenos'),
    path('cadastraruser/', views.cadastraruser, name='cadastraruser'),

    path('deletarnoticia/<int:noticia_pk>', views.deletarnoticia, name='deletarnoticia'),
]
