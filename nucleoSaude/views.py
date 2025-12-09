from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import LoginForm, RegistroForm
from django.contrib.messages import constants as message_constants

# Create your views here.
def home(request):
    return render(request,'home.html')

def formulario_contato_view(request):
    if request.method == 'POST':
        form = ContatoModelForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('contato_sucesso')
    
    else:
        form = ContatoModelForm()
        return render(request, 'contato/contatos.html', {'form': form})

def contato_sucesso_view(request):
    return render(request, 'contato/contato_sucesso.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = authenticate(
            request,
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        if user:
            login(request, user) 
            messages.success(request, 'Login Realizado')
            return redirect('login')
        messages.error(request, 'Credenciais inválidas')

    return render(request, 'login.html', {'form': form })

def registrar_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegistroForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        user = User.objects.create_user(
            username = form.cleaned_data['username'],
            email= form.cleaned_data['email'],
            password= form.cleaned_data['password'],
        )
        messages.success(request, 'Conta criada com sucesso.')
        return redirect('login')

    return render(request, 'registrar.html', {'form': form})

@login_required
def perfil(request):
    visitas = request.session.get('visitas', 0) + 1
    request.session['visitas'] = visitas
    return render(request, 'perfil.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu')
    return redirect('login')