from django.shortcuts import render, redirect, get_object_or_404
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


@login_required
def listar_refeicoes(request):
    if request.method == 'GET':
        usuario = request.user
        hoje = timezone.now().date()
        
        arranchamentos = Arranchamento.objects.filter(
            usuario=usuario, refeicao__data_refeicao__gte=hoje
        ).order_by('refeicao__data_refeicao')        
        
        return render(request, 'arranchamento/listar_refeicoes.html', {'arranchamentos': arranchamentos})

@login_required
def excluir_arranchamento(request, arranchamento_id):
    arranchamento = get_object_or_404(Arranchamento, id=arranchamento_id, usuario=request.user)
    
    if request.method == 'POST':
        arranchamento.delete()
        return redirect('listar_refeicoes')

    return redirect('listar_refeicoes')