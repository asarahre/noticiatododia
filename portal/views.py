from django.shortcuts import render, redirect

from portal.models import Noticia, Login
from portal.forms import NoticiaForm, CadastraUser, Cadastra


def home(request):
    return render(request, 'portal/home.html')


def dashboard(request):
    return render(request, 'portal/dashboard.html')


def noticia(request):
    noticia = Noticia.objects.all()
    context = {
        'noticia': noticia
    }
    return render(request, 'portal/noticia.html', context)


def excluirnoticia(request):
    noticia = Noticia.objects.all()
    context = {
        'noticia': noticia
    }
    return render(request, 'portal/excluirnoticia.html', context)


def deletarnoticia(request, noticia_pk):
    noticia = Noticia.objects.get(pk=noticia_pk)
    noticia.delete()

    return redirect('excluirnoticia')


def adicionarnoticia(request):
    form = NoticiaForm(request.POST or None, request.FILES or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'portal/adicionarnoticia.html', context)


def modificarnoticia(request):
    noticia = Noticia.objects.all()
    context = {
        'noticia': noticia
    }
    return render(request, 'portal/modificarnoticia.html', context)


def editar_noticia(request, noticia_pk):
    noticia = Noticia.objects.get(pk=noticia_pk)

    form = NoticiaForm(request.POST or None, request.FILES or None, instance=noticia)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('modificarnoticia')

    context = {
        'form': form,
    }

    return render(request, 'portal/editar_noticia.html', context)


def excluircomentario(request):
    return render(request, 'portal/excluircomentario.html')


def login(request):
    return render(request, 'portal/login.html')


def cadastro(request):
    login = Login.objects.all()

    context = {
        'login': login
    }
    return render(request, 'portal/cadastro.html', context)


def usuario(request):
    return render(request, 'portal/usuario.html')


def sobrenos(request):
    return render(request, 'portal/sobrenos.html')


def cadastraruser(request):
    form = CadastraUser(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }
    return render(request, 'portal/cadastraruser.html', context)


def editauser(request, login_pk):
    login = Login.objects.get(pk=login_pk)

    form = Cadastra(request.POST or None, instance=login)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('cadastro')

    context = {
        'form': form,
    }

    return render(request, 'portal/editauser.html', context)
