from django.shortcuts import render

def home(request):
    contexto = {
        'title' : 'Home '
    }

    return render(
        request,
        'home/index.html',
        contexto
    )
