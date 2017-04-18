from django.shortcuts import render
from .models import CPod

# Create your views here.

def inicial(request):
    cprod = CPod.objects.order_by('nome_cp')

    return render(request, 'controle/inicial.html', {'cprod': cprod})


