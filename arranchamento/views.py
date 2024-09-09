from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta, datetime
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'arranchamento/index.html')


def register_view(request):
    return render(request, 'arranchamento/register.html')


@login_required
def arranchar_usuario(request):
    if request.method == 'GET':
        hoje = datetime.today().date()
        primeiro_dia = hoje + timedelta(days=2) 
        dias = [primeiro_dia + timedelta(days=i) for i in range(15)]

        datas_formatadas = [dia.strftime('%Y-%m-%d') for dia in dias]


        return render(request, 'arranchamento/arranchamento.html', { 'datas': datas_formatadas })

    if request.method == 'POST':

        datas = request.POST.getlist('data_refeicao')
        tipos_refeicao = [request.POST.getlist(f'tipo_refeicao_{i}') for i in range(1, len(datas)+1)]
    
        if not datas or not any(tipos_refeicao):
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect('arranchar_usuario')

        for i, data in enumerate(datas):
            data_refeicao = timezone.datetime.strptime(data, '%Y-%m-%d').date()
            tipos = tipos_refeicao[i]

            for tipo in tipos:
                refeicao, created = Refeicao.objects.get_or_create(
                    tipo_refeicao=tipo,
                    data_refeicao=data_refeicao
                )

                arranchamento_existe = Arranchamento.objects.filter(usuario=request.user, refeicao=refeicao).exists()

                print(f"Tipo de Refeição: {refeicao.tipo_refeicao}, Data: {refeicao.data_refeicao}")

                if not arranchamento_existe:
                    Arranchamento.objects.create(usuario=request.user, refeicao=refeicao)
                    messages.success(request, f"Você foi inscrito para {refeicao.tipo_refeicao} no dia {refeicao.data_refeicao}.")
                else:
                    messages.warning(request, f"Você já está inscrito nesta refeição no dia {refeicao.data_refeicao}.")

        return redirect('listar_refeicoes')
    
    hoje = timezone.now().date()
    data_min = hoje + timedelta(days=2)
    data_max = hoje + timedelta(days=15)

    refeicoes_disponiveis = Refeicao.refeicoes_disponiveis()  # Obtém as refeições disponíveis

    # Passa as datas e as refeições disponíveis para o template
    return render(request, 'arranchamento.html', {
        'data_min': data_min,
        'data_max': data_max,
        'refeicoes_disponiveis': refeicoes_disponiveis
    })


@login_required
def listar_refeicoes(request):
    return render(request, 'arranchamento/listar_refeicoes.html')
