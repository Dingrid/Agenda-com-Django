from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date, timedelta
# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100) #cria o nome do evento
    descricao = models.TextField(blank=True, null=True) #a descricao do evento pode ser nula ou em branco
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    data_criacao = models.DateTimeField(auto_now=True) #insere a data atual do sistema
    usuario = models.ForeignKey(User, on_delete= models.CASCADE) #se o dono do evento for excluido vc exclui todos os eventos dele

    class Meta:
        db_table= 'evento' #o nome da tabela é evento

    def __str__(self): #apresenta no bd o titulo do evento na listagem
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime(' %d/%m/%Y %H:%M')

    def get_descricao_evento(self):
        return self.descricao

    def get_data_input_evento(self):
            return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now() - timedelta(hours=24):
            return True
        return False

    def get_evento_do_dia(self):
        if self.data_evento.strftime('%Y-%m-%d') == date.today().strftime('%Y-%m-%d'):
            return True
        return False
    