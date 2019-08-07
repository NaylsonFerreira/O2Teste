from django.contrib import admin
from .models import *

admin.site.register({Cargo,Candidato})
admin.site.register(Vaga,VagaAdmin)