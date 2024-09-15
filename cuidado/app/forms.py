from django.forms import ModelForm
from app.models import Tarefa

class TarefaForms(ModelForm):
    class Meta:
        model = Tarefa
        fields = ["titulo", "descricao", "enfermeira", "email"]