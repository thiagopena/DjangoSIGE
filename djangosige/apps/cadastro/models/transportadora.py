from django.db import models

from .base import UF_SIGLA, Pessoa


class Transportadora(Pessoa):
    class Meta:
        verbose_name = "Transportadora"


class Veiculo(models.Model):
    transportadora_veiculo = models.ForeignKey(
        "cadastro.Transportadora", related_name="veiculo", on_delete=models.CASCADE
    )
    descricao = models.CharField(max_length=255)
    placa = models.CharField(max_length=8, blank=True, null=True)
    uf = models.CharField(max_length=3, null=True, blank=True, choices=UF_SIGLA)

    def __unicode__(self):
        return f"{self.descricao} / {self.placa} / {self.uf}"

    def __str__(self):
        return f"{self.descricao} / {self.placa} / {self.uf}"
