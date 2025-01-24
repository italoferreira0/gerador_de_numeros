from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum


from .utils import gerar_numero
from .models import NumerosGerados


from django.views.generic import ListView
# Create your views here.

def processar_input(request):
    if request.method == 'POST':
        valorIncial = int(request.POST.get('valorIncial',1))
        valorFinal = int(request.POST.get('valorFinal'))

        numero = gerar_numero(valorIncial, valorFinal)

        if NumerosGerados.objects.filter(numeroGerado=numero).exists():
            return render(request, 'gerador/geradorExistente.html')

        NumerosGerados.objects.create( #colocar valor no banco de dados
            numeroGerado=numero
        )

        return render(request,'gerador/gerador.html',{'resultado': numero})
    else:   
        return HttpResponse(f'Falha no envio.')

def viewGerador(request):
    processar_input(request)
    return render(request,'gerador/gerador.html')

def geradorExistente(request):
    return render(request,'gerador/geradorExistente')

class GeradorListView(ListView):
    model = NumerosGerados
    template_name = 'gerador/geradorLista.html'
    context_object_name = 'numerosGerados'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)            
        soma_total = NumerosGerados.objects.aggregate(Sum('numeroGerado'))['numeroGerado__sum'] or 0
        context['soma_total'] = soma_total
            
        return context