from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import json
from django.views.decorators.csrf import csrf_exempt
from .models import User as UserModel

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data["username"]
        password = data["password"]

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
            def verificar_login(username, password):
                try:
                    usuario = UserModel.objects.get(username=username, password=password)
                    return True, usuario 
                except UserModel.DoesNotExist:
                    return False, None  

            u = username
            p = password
            login_valido, usuario = verificar_login(u, p)

            if login_valido:
                print("Login válido para o usuário:", usuario.username)
                return JsonResponse({'success': True, 'message': 'Foi! '})
            else:
                print("Usuário ou senha incorretos.")
                return JsonResponse({'success': False, 'message': 'Erro, Usuário ou senha incorretos! '})
            