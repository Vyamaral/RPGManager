from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Personagem
from .forms import PersonagemForm, CadastroForm


@login_required
def listar_personagens(request):

    if request.user.is_superuser:
        personagens = Personagem.objects.all()
    else:
        personagens = Personagem.objects.filter(
            usuario=request.user
        )

    return render(
        request,
        'fichas/lista.html',
        {'personagens': personagens}
    )


@login_required
def criar_personagem(request):
    form = PersonagemForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():
        personagem = form.save(commit=False)
        personagem.usuario = request.user
        personagem.save()
        return redirect('lista')

    return render(
        request,
        'fichas/criar.html',
        {'form': form}
    )


@login_required
def editar_personagem(request, id):

    if request.user.is_superuser:
        personagem = get_object_or_404(
            Personagem,
            id=id
        )
    else:
        personagem = get_object_or_404(
            Personagem,
            id=id,
            usuario=request.user
        )

    form = PersonagemForm(
        request.POST or None,
        request.FILES or None,
        instance=personagem
    )

    if form.is_valid():
        form.save()
        return redirect('lista')

    return render(
        request,
        'fichas/editar.html',
        {
            'form': form,
            'personagem': personagem
        }
    )


@login_required
def excluir_personagem(request, id):

    if request.user.is_superuser:
        personagem = get_object_or_404(
            Personagem,
            id=id
        )
    else:
        personagem = get_object_or_404(
            Personagem,
            id=id,
            usuario=request.user
        )

    if request.method == 'POST':
        personagem.delete()
        return redirect('lista')

    return render(
        request,
        'fichas/excluir.html',
        {'personagem': personagem}
    )


def cadastro(request):

    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = CadastroForm()

    return render(
        request,
        'fichas/cadastro.html',
        {'form': form}
    )