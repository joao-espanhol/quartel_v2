from django import forms
from .models import Refeicao, CustomUser, POSTOS_GRADUACOES, Arranchamento
from django.contrib.auth.forms import UserCreationForm


class ArranchamentoForm(forms.Form):
    tipo_refeicao = forms.ChoiceField(choices=Refeicao.TIPO_REFEICAO)
    data_refeicao = forms.DateField()

    def save(self, usuario):
        tipo_refeicao = self.cleaned_data['tipo_refeicao']
        data_refeicao = self.cleaned_data['data_refeicao']

        # Verificar se a refeição já existe
        refeicao, created = Refeicao.objects.get_or_create(
            tipo_refeicao=tipo_refeicao,
            data_refeicao=data_refeicao
        )

        # Criar a inscrição para o usuário na refeição
        arranchamento = Arranchamento.objects.create(usuario=usuario, refeicao=refeicao)
        return arranchamento


class CustomUserCreationForm(UserCreationForm):
    nome = forms.CharField(required=True)
    nome_guerra = forms.CharField(required=True)
    posto = forms.ChoiceField(choices=POSTOS_GRADUACOES, required=True)
    subunidade = forms.ChoiceField(choices=POSTOS_GRADUACOES, required=True)

    class Meta:
        model = CustomUser
        fields = ('idt_mil', 'password1', 'password2', 'nome', 'nome_guerra', 'posto', 'subunidade')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.nome = self.cleaned_data.get('nome')
        user.nome_guerra = self.cleaned_data.get('nome_guerra')
        user.posto = self.cleaned_data.get('posto')
        user.subunidade = self.cleaned_data.get('subunidade')

        if commit:
            user.save()
        return user


