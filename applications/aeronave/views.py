

# Create your views here.

from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from applications.aeronave.models import aeronave

class aeronaveForm(ModelForm):
    class Meta:
        model = aeronave
        fields = [
            'name',
            'num_max',
        ]

def aeronaveList(request, template_name = 'aeronave_list.html'):
    aeronaves = aeronave.objects.all()
    data = { }
    data['object_list'] = aeronaves
    return render(request, template_name, data)

def aeronave_create(request, template_name = 'Crear_Aeronave.html'):
    form = aeronaveForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_aeronaves')
    return render(request, template_name, {'form': form})

def aeronave_update(request, pk, template_name='Crear_Aeronave.html'):
    aeronave_update = get_object_or_404(aeronave, pk=pk)
    form = aeronaveForm(request.POST or None, instance=aeronave_update)
    if form.is_valid():
        form.save()
        return redirect('lista_aeronaves')
    return render(request, template_name, {'form': form})

def aeronave_delete(request, pk, template_name = 'Borrar_Aeronave.html'):
    aeronave_borrar = get_object_or_404(aeronave, pk=pk)
    if request.method=='POST':
        aeronave_borrar.delete()
        return redirect('aeronave:aeronaveList')
    return render(request, template_name, {'object': aeronave_borrar})
