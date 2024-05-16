import re
from django.shortcuts import render
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
            return JsonResponse({'success': True, 'message': 'Login bem-sucedido!'})
        else:
            return JsonResponse({'success': False, 'message': 'Credenciais inválidas.'})
    else:
        return JsonResponse({'success': False, 'message': 'Método de solicitação não suportado.'})