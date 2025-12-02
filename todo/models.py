from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    importancia = models.CharField(choices=[('alta', 'Alta'), ('media', 'Media'), ('baixa', 'Baixa')], max_length=5, default='media') 
    data_created = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
