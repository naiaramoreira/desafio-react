from django.db import models

class Book(models.Model):
    title = models.TextField(max_length=32, blank=False, null=False)

class Food(models.Model):
    nome = models.TextField(max_length=32, blank=False, null=False)
    quantidade = models.IntegerField(blank=False, null=False)
    proteinas = models.IntegerField(blank=False, null=False)
    carboidratos = models.IntegerField(blank=False, null=False)
    gordura = models.IntegerField(blank=False, null=False)