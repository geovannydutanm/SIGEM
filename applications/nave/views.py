from django.shortcuts import render
from django.http import  HttpResponse
from .models import Naves

#from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

# Create your views here.

def NaveView(request):
    nave = Naves.objects.all()
    return  render(request,'listaNave.html')

class naveForm(ModelForm):
    class Meta:
        model = Naves
        fields = [
            'name',
        ]

def naveList(request, template_name = 'listaNave.html'):
    nave = Naves.objects.all()
    data = { }
    data['object_list'] = nave
    return render(request, template_name, data)

def nave_create(request, template_name = 'naveNueva.html'):
    form = naveForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_nave')
    return render(request, template_name, {'form': form})

def nave_update(request, pk, template_name='nave_Nueva.html'):
    nave_update = get_object_or_404(Naves, pk=pk)
    form = naveForm(request.POST or None, instance=nave_update)
    if form.is_valid():
        form.save()
        return redirect('lista_nave')
    return render(request, template_name, {'form': form})

def aeronave_delete(request, pk, template_name = 'Borrar_Nave.html'):
    nave_borrar = get_object_or_404(Naves, pk=pk)
    if request.method=='POST':
        nave_borrar.delete()
        return redirect('nave:listaNave')
    return render(request, template_name, {'object': nave_borrar})