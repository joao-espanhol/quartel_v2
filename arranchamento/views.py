from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'arranchamento/index.html')


def register_view(request):
    return render(request, 'arranchamento/register.html')


@login_required
def arranchar_usuario(request):
    if request.method == 'GET':
        return render(request, 'arranchamento/arranchamento.html')

    if request.method == 'POST':
        tipo_refeicao = request.POST['tipo_refeicao']
        data_refeicao = request.POST['data_refeicao']
        print(f"Tipo de Refeição: {tipo_refeicao}, Data: {data_refeicao}")


        if tipo_refeicao and data_refeicao:
            data_refeicao = timezone.datetime.strptime(data_refeicao, '%Y-%m-%d').date()

            # Verifica se a refeição já existe, se não, cria uma nova
            refeicao, created = Refeicao.objects.get_or_create(
                tipo_refeicao=tipo_refeicao,
                data_refeicao=data_refeicao
            )

            arranchamento_existe = Arranchamento.objects.filter(usuario=request.user, refeicao=refeicao).exists()
            

            if not arranchamento_existe:
                    # Cria a inscrição
                inscricao = Arranchamento.objects.create(usuario=request.user, refeicao=refeicao)
                messages.success(request, f"Você foi inscrito para {refeicao.tipo_refeicao} no dia {refeicao.data_refeicao}.")
            else:
                messages.warning(request, "Você já está inscrito nesta refeição.")
        else:
            messages.error(request, "Todos os campos são obrigatórios.")

        # Redireciona após o POST para evitar o reenvio do formulário
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
