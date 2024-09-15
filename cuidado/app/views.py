from django.shortcuts import render, redirect
from app.forms import TarefaForms
from app.models import Tarefa
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    data = {}
    #data['db'] = Tarefa.objects.all()
    all = Tarefa.objects.all()
    paginator = Paginator(all, 3)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)

def forms(request):
    data = {}
    data ['form'] = TarefaForms()
    return render(request, 'forms.html', data)

def create(request):
    form = TarefaForms(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def edit(request, pk):
    data = {}
    data['db'] = Tarefa.objects.get(pk=pk)
    data['form'] = TarefaForms(instance=data['db'])
    return render(request,'forms.html', data)

def update(request,pk):
    data = {}
    data['db'] = Tarefa.objects.get(pk=pk)
    form = TarefaForms(request.POST or None , instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Tarefa.objects.get(pk=pk)
    db.delete()
    return redirect('home')