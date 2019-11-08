# render es un metodo que toma un request
from django.shortcuts import render

# library utilities
from datetime import datetime


posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]

# Si no estamos logiados este metodo por defecto nos va llevar
# a la vista que tengamos en setting/Login_url


def list_posts(request):
    """la clase feed.html es encontrada por si sola siempre
     y cuando la carpeta donde esta se llame template """
    # Esta condicion es para que cuando el usuario no este logiado no lo deje entrar a la vista
    if not request.user.is_authenticated:
        return render(request, 'User/login.html')

    return render(request, 'post/feed.html', {'posts': posts})

