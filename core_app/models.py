from django.db import models
from django.contrib import admin
from django.utils.html import format_html

from storages.backends.ftp import FTPStorage
from django.urls import reverse
SERVIDOR_FTP_WEB = FTPStorage()

class Cargo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    def get_absolute_url(self):
        return reverse('core_app:Index')
    def __str__(self):
        return self.nome

class Vaga(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    salario = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('core_app:Index')
    def __str__(self):
        return str(self.nome)+" "+str(self.cargo)

    def cargo_property(self):
        return str(self.cargo)
    cargo_ = property(cargo_property)

    def candidatos_property(self):
        lista = Candidato.objects.all().filter(vaga=self.id)
        candidatos = []
        for i in lista:
            candidatos.append("<a href='/admin/core_app/candidato/"+str(i.id)+"'>"+i.nome+"</a>")
        candidatos = str(candidatos).replace("\"","").replace("[","").replace("]","")
        return format_html(candidatos)
    candidatos = property(candidatos_property)

class VagaAdmin(admin.ModelAdmin):
    list_display = ('__str__','cargo_','candidatos')
    list_display_links = ('__str__','cargo_')
    empty_value_display = '--'

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    curriculo = models.FileField(upload_to='curriculos/',storage=SERVIDOR_FTP_WEB)
    def get_absolute_url(self):
        return reverse('core_app:Index')
    def __str__(self):
        return self.nome
