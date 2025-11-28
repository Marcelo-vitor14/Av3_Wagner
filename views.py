
from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CadastroUsuarioForm, EnderecoForm
from .forms_auth import LoginForm 


def cadastro_usuario(request):
    if request.method == 'POST':
        user_form = CadastroUsuarioForm(request.POST)
        endereco_form = EnderecoForm(request.POST)
        
        if user_form.is_valid() and endereco_form.is_valid():
            try:
                with transaction.atomic():
                    endereco_instance = endereco_form.save()
                    user_instance = user_form.save(commit=False)
                    user_instance.endereco = endereco_instance
                    user_instance.set_password(user_form.cleaned_data["password2"])
                    user_instance.save()
                    messages.success(request, 'Cadastro realizado com sucesso! Faça login.')
                    return redirect('login_page')
            except Exception as e:
                messages.error(request, f'Erro ao salvar: {e}')
                
    else:
        user_form = CadastroUsuarioForm()
        endereco_form = EnderecoForm()

    context = {
        'user_form': user_form,
        'endereco_form': endereco_form,
        'title': 'Cadastro'
    }
    return render(request, 'cadastro/cadastro.html', context)


def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) 
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo(a), {user.nome_completo.split()[0]}!')
                return redirect('home_page')
            else:
                messages.error(request, 'E-mail ou senha inválidos.')
    else:
        form = LoginForm()

    context = {'form': form, 'title': 'Login'}
    return render(request, 'usuarios/login.html', context)


def user_logout(request):
    logout(request)
    messages.info(request, "Você saiu do sistema.")
    return redirect('login_page')

def recuperar_senha(request):
    context = {'title': 'Recuperar Senha'}
    return render(request, 'usuarios/recuperacao_senha.html', context)


@login_required 
def home_page(request):
    context = {
        'title': 'Painel Administrativo',
        'usuario': request.user,
        'cargo': 'Administrador' if request.user.is_superuser else 'Usuário Padrão'
    }
    return render(request, 'usuarios/PainelAdmin.html', context)


def modelo_page(request):
    context = {
        'title': 'Modelo Padrão',
        'mensagem': 'Este é o conteúdo do Modelo '
    }
    return render(request, 'usuarios/Modelo.html', context)


def tela_inicial(request):
    return render(request, "tela_inicial.html")