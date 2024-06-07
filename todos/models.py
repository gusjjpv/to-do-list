from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    # null=False vai obrigar o campo a ser preenchido, blank=False vai obrigar o campo a ser preenchido, n aceitando espaços em branco.
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    # auto_now_add=True vai adicionar a data e hora atual quando o objeto for criado.
    deadline = models.DateTimeField(null=True, blank=True)
    finishead = models.DateTimeField(null=True)
