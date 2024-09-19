from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.conf import settings
from users.models import CustomUser


class Refeicao(models.Model):
    TIPO_REFEICAO = [
    ('CAFE', 'Café da Manhã'),
    ('ALMO', 'Almoço'),
    ('JANT', 'Jantar'),
    ('CEIA', 'Ceia'),
]

    tipo_refeicao = models.CharField(max_length=4, choices=TIPO_REFEICAO)
    data_refeicao = models.DateField()

    class Meta:
        unique_together = ('tipo_refeicao', 'data_refeicao')

    def __str__(self):
        return f'{self.get_tipo_refeicao_display()} - {self.data_refeicao}'

    
    @staticmethod
    def refeicoes_disponiveis():
        """Retorna refeições disponíveis entre 2 e 15 dias à frente."""
        hoje = timezone.now().date()
        return Refeicao.objects.filter(
            data_refeicao__range=(hoje + timedelta(days=2), hoje + timedelta(days=15))
        )


class Arranchamento(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    refeicao = models.ForeignKey(Refeicao, on_delete=models.CASCADE)
    data_arranchamento = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'refeicao')

    def __str__(self):
        return f"{self.usuario} inscrito em {self.refeicao}"