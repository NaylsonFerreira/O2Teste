from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView,CreateView,UpdateView
from .models import *

def index(request):
    candidatos = Candidato.objects.all()
    contexto = {
        "candidatos":candidatos,
    }
    return render(request,'core_app/index.html',contexto)

class CandidatoCreate(CreateView):
    model = Candidato
    fields = '__all__'
    template_name = 'core_app/form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cabecalho'] = "Cadastrar Candidato"
        return context

class CandidatoUpdateView(UpdateView):
    model = Candidato
    fields = '__all__'
    template_name = 'core_app/form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cabecalho'] = "Alterar Candidato"
        return context

class CandidatoDeleteView(DeleteView):
    model = Candidato
    success_url = '/'
    template_name = 'core_app/confirm_delete.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cabecalho'] = "Excluir Candidato"
        return context