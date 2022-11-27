from django.shortcuts import render, HttpResponse
from django.db.models import Q
from .models import tabplaca

# Create your views here.
""" def index(request):
    data = request.GET.get('numplaca')
    try:
        datos = data
        objeto = tabplaca.objects.get(colplaca=datos)
        print(data) 
        data = (objeto.colplaca)
    except:
        data = data
        print(data)   
    return render(request, 'index.html',{'data':data}) """
def index(request):
    wbplaca = request.GET.get("numplaca")
    print(wbplaca)
    qryplaca = tabplaca.objects.values_list('colplaca')
    "print(qryplaca)"
    if wbplaca:
        qryplaca = tabplaca.objects.filter(
            Q(colplaca__icontains = wbplaca)
        ).distinct()
        valor = list(qryplaca.values_list('colplaca'))   
        responder = ["Su placa"] + valor + ["esta disponible para ser retirada"] 
        return render(request, 'index.html', {'qryplaca':responder})
    else:
        responder = "No esta disponible"
        return render(request, 'index.html', {'qryplaca':responder})