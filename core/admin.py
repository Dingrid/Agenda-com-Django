from django.contrib import admin
from core.models import Evento

# Register your models here.



class EventoAdmin(admin.ModelAdmin):
    #apresenta no bd o titulo e as datas do evento na listagem
    list_display = ('id','titulo', 'data_evento', 'data_criacao')
    #Cria um filtro para filtrar por nome de usuario, titulo e data de evento
    list_filter = ('usuario', 'titulo', 'data_evento',)

admin.site.register(Evento, EventoAdmin)
