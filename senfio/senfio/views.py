import re
from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def entrou(request):
    return render(request, 'entrou.html')


def login(request):
    if request.method == 'POST':
        data = request.POST 
        email = data.get('username')  # Recebendo o email do frontend
        password = data.get('password')

        # Verificar se o email segue o formato desejado
        if not re.match(r'^[a-zA-Z0-9._%+-]+@senfio\.com$', email):
            return JsonResponse({'success': False, 'message': 'Por favor, insira um email válido no formato nome.sobrenome@senfio.com'})

        if email == 'admin@senfio.com' and password == 'admin':  # Ajuste as credenciais conforme necessário
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Credenciais inválidas'})

    # Adicione um retorno padrão para o caso de a solicitação não ser POST
    return JsonResponse({'success': False, 'message': 'Método de solicitação não suportado'})