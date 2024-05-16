from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def entrou(request):
    return render(request, 'entrou.html')

def login(request):
    if request.method == 'POST':
        data = request.POST 
        username = data.get('username')
        password = data.get('password')

        if username == 'admin' and password == 'admin':
            return render(request, 'index.html', {'success': True})
        else:
            return render(request, 'index.html', {'success': False, 'message': 'Credenciais inválidas'})
