from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name="Título",max_length=100, null=False, blank=False)
    # null=False vai obrigar o campo a ser preenchido, blank=False vai obrigar o campo a ser preenchido, n aceitando espaços em branco.
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    # auto_now_add=True vai adicionar a data e hora atual quando o objeto for criado.
    deadline = models.DateField(verbose_name="Data de Entrega",null=True, blank=True)
    finishead = models.DateField(null=True)
