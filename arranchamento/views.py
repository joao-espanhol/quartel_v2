<<<<<<< HEAD
<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta, datetime
from django.contrib import messages
from django.db.models import Case, When, IntegerField
from babel.dates import format_date
import calendar
<<<<<<< HEAD
from .models import *

@login_required
=======
from django.shortcuts import render, redirect
=======
from django.shortcuts import render, redirect, get_object_or_404
>>>>>>> fa0a5d4 (View listar_refeicoes funcionando com a funcionalidade cancelar refeicoes)
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta, datetime
from django.contrib import messages
=======
>>>>>>> e6860c8 (Alterações no formato de apresentação das datas)
from .models import *

<<<<<<< HEAD
>>>>>>> 56be9eb (Primeiro commit: adicionando todos os arquivos do projeto)
=======
@login_required
>>>>>>> d7522b7 (Correcao Login/Logout e estética visual)
def index(request):
    return render(request, 'arranchamento/index.html')


def register_view(request):
    return render(request, 'arranchamento/register.html')


@login_required
def arranchar_usuario(request):
    if request.method == 'GET':
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 384db94 (Funcionando Medio)
        hoje = datetime.today().date()
        primeiro_dia = hoje + timedelta(days=2) 
        dias = [primeiro_dia + timedelta(days=i) for i in range(15)]

<<<<<<< HEAD
<<<<<<< HEAD
        datas_formatadas = [dia.strftime('%d/%m/%Y') for dia in dias]
        dias_semana = [format_date(dia, format='full', locale='pt_BR').split(',')[0].capitalize() for dia in dias]

        datas_completas = zip(datas_formatadas, dias_semana)

        contexto = {
            'datas_completas': datas_completas,  # Passando a lista de pares
        }

        return render(request, 'arranchamento/arranchamento.html', contexto)

    if request.method == 'POST':

        datas = request.POST.getlist('data_refeicao')
        tipos_refeicao = [request.POST.getlist(f'tipo_refeicao_{i}') for i in range(1, len(datas)+1)]
    
        if not datas or not any(tipos_refeicao):
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect('arranchar_usuario')

        for i, data in enumerate(datas):
            data_refeicao = timezone.datetime.strptime(data, '%d/%m/%Y').date()
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
=======
        return render(request, 'arranchamento/arranchamento.html')
=======
        datas_formatadas = [dia.strftime('%Y-%m-%d') for dia in dias]
=======
        datas_formatadas = [dia.strftime('%d/%m/%Y') for dia in dias]
        dias_semana = [format_date(dia, format='full', locale='pt_BR').split(',')[0].capitalize() for dia in dias]
>>>>>>> e6860c8 (Alterações no formato de apresentação das datas)

        datas_completas = zip(datas_formatadas, dias_semana)

<<<<<<< HEAD
        return render(request, 'arranchamento/arranchamento.html', { 'datas': datas_formatadas })
>>>>>>> 384db94 (Funcionando Medio)
=======
        contexto = {
            'datas_completas': datas_completas,  # Passando a lista de pares
        }

        return render(request, 'arranchamento/arranchamento.html', contexto)
>>>>>>> e6860c8 (Alterações no formato de apresentação das datas)

    if request.method == 'POST':

        datas = request.POST.getlist('data_refeicao')
        tipos_refeicao = [request.POST.getlist(f'tipo_refeicao_{i}') for i in range(1, len(datas)+1)]
    
        if not datas or not any(tipos_refeicao):
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect('arranchar_usuario')

        for i, data in enumerate(datas):
            data_refeicao = timezone.datetime.strptime(data, '%d/%m/%Y').date()
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
<<<<<<< HEAD
    
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
>>>>>>> 56be9eb (Primeiro commit: adicionando todos os arquivos do projeto)
=======
>>>>>>> fa0a5d4 (View listar_refeicoes funcionando com a funcionalidade cancelar refeicoes)


@login_required
def listar_refeicoes(request):
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> fa0a5d4 (View listar_refeicoes funcionando com a funcionalidade cancelar refeicoes)
    if request.method == 'GET':
        usuario = request.user
        hoje = timezone.now().date()
        
<<<<<<< HEAD
<<<<<<< HEAD
        arranchamentos = Arranchamento.objects.filter(
            usuario=usuario, refeicao__data_refeicao__gte=hoje
        ).annotate(
            tipo_ordem=Case(
                When(refeicao__tipo_refeicao='CAFE', then=0),
                When(refeicao__tipo_refeicao='ALMO', then=1),
                When(refeicao__tipo_refeicao='JANT', then=2),
                When(refeicao__tipo_refeicao='CEIA', then=3),
                output_field=IntegerField(),
            )
        ).order_by('refeicao__data_refeicao', 'tipo_ordem')
        
=======
        arranchamentos = Arranchamento.objects.filter(usuario=usuario, refeicao__data_refeicao__gte=hoje)
>>>>>>> fa0a5d4 (View listar_refeicoes funcionando com a funcionalidade cancelar refeicoes)
=======
        arranchamentos = Arranchamento.objects.filter(
            usuario=usuario, refeicao__data_refeicao__gte=hoje
        ).annotate(
            tipo_ordem=Case(
                When(refeicao__tipo_refeicao='CAFE', then=0),
                When(refeicao__tipo_refeicao='ALMO', then=1),
                When(refeicao__tipo_refeicao='JANT', then=2),
                When(refeicao__tipo_refeicao='CEIA', then=3),
                output_field=IntegerField(),
            )
        ).order_by('refeicao__data_refeicao', 'tipo_ordem')
        
>>>>>>> 1a0e58f (Melhora visual, com a inclusao do footer e navbar)
        return render(request, 'arranchamento/listar_refeicoes.html', {'arranchamentos': arranchamentos})

@login_required
def excluir_arranchamento(request, arranchamento_id):
    arranchamento = get_object_or_404(Arranchamento, id=arranchamento_id, usuario=request.user)
    
    if request.method == 'POST':
        arranchamento.delete()
        return redirect('listar_refeicoes')

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 700e20e (Arranchamentos do Dia funcionando)
    return redirect('listar_refeicoes')


@login_required
def verificar_arranchamentos(request):
    if request.method == 'GET':
        hoje = timezone.now().date()
<<<<<<< HEAD
<<<<<<< HEAD
        primeiro_dia = hoje + timedelta(days=0)
=======
        primeiro_dia = hoje + timedelta(days=3) 
>>>>>>> 700e20e (Arranchamentos do Dia funcionando)
=======
        primeiro_dia = hoje + timedelta(days=0)
>>>>>>> 98cfd25 (Arranchamento do Dia para Hoje)
        
        ordem_postos = {
            'Soldado': 1,
            'Cabo': 2,
            'Sargento': 3,
            'Subtenente': 4,
            'Aspirante': 5,
            'Segundo Tenente': 6,
            'Primeiro Tenente': 7,
            'Capitão': 8,
            'Major': 9,
            'Tenente-Coronel': 10,
            'Coronel': 11,
            'General de Brigada': 12,
            'General de Divisão': 13,
            'General de Exército': 14,
        }
        
        arranchamentos = Arranchamento.objects.filter(
            refeicao__data_refeicao=primeiro_dia
        ).annotate(
            tipo_ordem=Case(
                When(refeicao__tipo_refeicao='CAFE', then=0),
                When(refeicao__tipo_refeicao='ALMO', then=1),
                When(refeicao__tipo_refeicao='JANT', then=2),
                When(refeicao__tipo_refeicao='CEIA', then=3),
                output_field=IntegerField(),
            ),
            ordem_postos=Case(
                *[When(usuario__posto=posto, then=valor) for posto, valor in ordem_postos.items()],
                output_field=IntegerField(),
            )
        ).order_by('tipo_ordem', 'usuario__subunidade', 'ordem_postos')

        return render(request, 'arranchamento/arranchamentos_dia.html', {'arranchamentos': arranchamentos})
<<<<<<< HEAD
=======
    return render(request, 'arranchamento/listar_refeicoes.html')
>>>>>>> 56be9eb (Primeiro commit: adicionando todos os arquivos do projeto)
=======
    return redirect('listar_refeicoes')
>>>>>>> fa0a5d4 (View listar_refeicoes funcionando com a funcionalidade cancelar refeicoes)
=======
>>>>>>> 700e20e (Arranchamentos do Dia funcionando)
