# usuarios/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Endereco(models.Model):
    cep = models.CharField(max_length=9, verbose_name="CEP")
    rua = models.CharField(max_length=255, verbose_name="rua")
    bairro = models.CharField(max_length=255, verbose_name="Bairro")
    localidade = models.CharField(max_length=255, verbose_name="Cidade")
    uf = models.CharField(max_length=2, verbose_name="Estado (UF)")
    numero = models.CharField(max_length=10, verbose_name="Número")
    complemento = models.CharField(max_length=255, blank=True, null=True, verbose_name="Complemento")

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
    
    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cep}"

class Usuario(AbstractUser):
    TIPO_DEFICIENCIA_CHOICES = [
        ('AUDITIVA', 'Auditiva'),
        ('VISUAL', 'Visual'),
        ('FISICA', 'Física'),
        ('NENHUMA', 'Nenhuma'),
    ]

  
    nome_completo = models.CharField(max_length=255, verbose_name="Nome Completo")
    idade = models.IntegerField(null=True, blank=True, verbose_name="Idade")
    tipo_deficiencia = models.CharField(
        max_length=10,
        choices=TIPO_DEFICIENCIA_CHOICES,
        default='NENHUMA',
        verbose_name="Tipo de Deficiência"
    )
    telefone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefone")
    
 
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Endereço")
    
 
    email = models.EmailField(unique=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome_completo'] 

    def __str__(self):
        return self.email