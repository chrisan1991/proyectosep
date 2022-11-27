from django.shortcuts import render, HttpResponse
from django.db.models import Q
from .models import tabplaca

# Create your views here.


def index(request):
    if request.GET.get("numplaca"):
        wbplaca = request.GET.get("numplaca")
        qryplaca = tabplaca.objects.values_list('colplaca')
        qryplaca = tabplaca.objects.filter(
            Q(colplaca__icontains = wbplaca)
        ).distinct()
        #valor = list(qryplaca.values_list('colplaca'))   
        # responder = ["Su placa"] + valor + ["esta disponible para ser retirada"]
        return render(request, 'index.html', {'qryplaca':qryplaca})
    else:
        responder = "No has realizado ninguna busqueda"
        return render(request, 'index.html', {'messages':responder})