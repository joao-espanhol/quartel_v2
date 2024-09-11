from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser, BaseUserManager

POSTOS_GRADUACOES = [
    ('Gen Ex', 'General de Exército'),
    ('Gen Div', 'General de Divisão'),
    ('Gen Bda', 'General de Brigada'),
    ('Cel', 'Coronel'),
    ('Ten Cel', 'Tenente Coronel'),
    ('Maj', 'Major'),
    ('Cap', 'Capitão'),
    ('1º Ten', '1º Tenente'),
    ('2º Ten', '2º Tenente'),
    ('Asp', 'Aspirante'),
    ('S Ten', 'Subtenente'),
    ('1º Sgt', '1º Sargento'),
    ('2º Sgt', '2º Sargento'),
    ('3º Sgt', '3º Sargento'),
    ('Cb', 'Cabo'),
    ('Sd', 'Soldado'),
]

SUBUNIDADES = [
    ('1ª Cia Fuz Mec', '1ª Companhia de Fuzileiros Mecanizada'),
    ('2ª Cia Fuz Mec', '2ª Companhia de Fuzileiros Mecanizada'),
    ('Cia C Ap', 'Companhia de Comando e Apoio'),
    ('SIBld', 'Seção de Instrução de Blindados'),
    ('NPOR', 'Núcleo de Preparação de Oficiais da Reserva'),
    ('CIOU', 'Centro de Instrução de Operações Urbanas'),
    ('EM', 'Estado Maior'),
]

class CustomUserManager(BaseUserManager):
    def create_user(self, idt_mil, password=None, **extra_fields):
        if not idt_mil:
            raise ValueError('O campo IDT Militar deve ser preenchido')
        user = self.model(idt_mil=idt_mil, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, idt_mil, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário deve ter is_superuser=True.')

        return self.create_user(idt_mil, password, **extra_fields)

class CustomUser(AbstractUser):
    idt_mil = models.CharField(max_length=10, unique=True)
    subunidade = models.CharField(max_length=20, choices=SUBUNIDADES)
    posto = models.CharField(max_length=20, choices=POSTOS_GRADUACOES)
    nome = models.CharField(max_length=100)
    nome_guerra = models.CharField(max_length=100)

    class UserType(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        SARGENTEANTE = 'sargenteante', 'Sargenteante'
        COMUM = 'comum', 'Comum'
        RANCHEIRO = 'rancheiro', 'Rancheiro'

    user_type = models.CharField(
        max_length=50,
        choices=UserType.choices,
        default=UserType.COMUM
    )

    USERNAME_FIELD = 'idt_mil' 
    REQUIRED_FIELDS = ['posto', 'nome', 'nome_guerra', 'subunidade']

    username = None

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups', 
        blank=True,
        help_text='Os grupos aos quais este usuário pertence.',
        verbose_name='grupos'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True,
        help_text='Permissões específicas para este usuário.',
        verbose_name='permissões de usuário'
    )

    def __str__(self):
        return f'{self.posto} {self.nome_guerra}'
=======

# Create your models here.
>>>>>>> 1a0e58f (Melhora visual, com a inclusao do footer e navbar)
