from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import JsonResponse
import json

def index(request):
    return render(request, 'index.html')

def entrou(request):
    return render(request, 'entrou.html')

def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data["username"]
        password = data["password"]

        # Adicione logs de depuração para verificar os dados recebidos
        print("Dados recebidos - Username:", username)
        print("Dados recebidos - Password:", password)
        
        if not username.endswith('@senfio.com') or '.' not in username[:username.index('@')] or len(password) < 8:
            if not username.endswith('@senfio.com'):
                return JsonResponse({'success': False, 'message': 'O email deve ser institucional (terminar com @senfio.com).'})
            elif '.' not in username[:username.index('@')]:
                return JsonResponse({'success': False, 'message': 'O email deve conter nome e sobrenome separados por ponto antes do domínio.'})
            elif len(password) < 8:
                return JsonResponse({'success': False, 'message': 'A senha deve conter no mínimo 8 caracteres.'})
            else:
                # Redirecionar para a página entrou.html se o login for bem-sucedido
                print("\nboa\n")
                return redirect('/entrou/')
    return render(request, 'login_view.html')