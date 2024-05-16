from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def entrou(request):
    return render(request, 'entrou.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Adicione logs de depuração para verificar os dados recebidos
        print("Dados recebidos - Username:", username)
        print("Dados recebidos - Password:", password)
        
        # Verificação de nome de usuário e senha
        if username == 'rodrigo' and password == 'rodrigo':
            # Redirecionar para a página entrou.html se o login for bem-sucedido
            return redirect('entrou')
        else:
            return JsonResponse({'success': False, 'message': 'Credenciais inválidas.'})
    else:
        return JsonResponse({'success': False, 'message': 'Método de solicitação não suportado.'})