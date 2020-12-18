#from django.shortcuts import render


#from __future__ import unicode_literals

#  BACKEND AERONAVE
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from marcial.models import Nave, Aeronave, Pasajero, Aeronave_Pasajero, Revision

def index(request):
    return render(request, template_name='index.html', context= {})

#BACKEND NAVE
def list_nave(request):
    nave = Nave.objects.all()
    return render(request, template_name='nave/list_nave.html', context= {'nave':nave})

class naveForm(ModelForm):
    class Meta:
        model = Nave
        fields = [
            'name',
        ]

def create_nave(request, template_name = 'nave/create_nave.html'):
    form = naveForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_nave')
    return render(request, template_name, {'form': form})

def update_nave(request, pk, template_name='nave/create_nave.html'):
    nave_update = get_object_or_404(Nave, pk=pk)
    form = naveForm(request.POST or None, instance=nave_update)
    if form.is_valid():
        form.save()
        return redirect('list_nave')
    return render(request, template_name, {'form': form})


#AERONAVE
def list_aeronave(request):
    aeronave = Aeronave.objects.all()
    return render(request, template_name='aeronave/list_aeronave.html', context= {'aeronave':aeronave})

class aeronaveForm(ModelForm):
    class Meta:
        model = Aeronave
        fields = [
            'name',
            'num_max',
            'nave_origen',
            'nave_destino',

        ]

def create_aeronave(request, template_name = 'aeronave/create_aeronave.html'):
    form = aeronaveForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_aeronave')
    return render(request, template_name, {'form': form})

def update_aeronave(request, pk, template_name='aeronave/create_aeronave.html'):
    aeronave_update = get_object_or_404(Aeronave, pk=pk)
    form = aeronaveForm(request.POST or None, instance=aeronave_update)
    if form.is_valid():
        form.save()
        return redirect('list_aeronave')
    return render(request, template_name, {'form': form})

def delete_aeronave(request, pk, template_name = 'aeronave/delete_aeronave.html'):
    aeronave_borrar = get_object_or_404(Aeronave, pk=pk)
    if request.method=='POST':
        aeronave_borrar.delete()
        return redirect('list_aeronave')
    return render(request, template_name, {'object': aeronave_borrar})


#PASAJERO
def list_pasajero(request):
    pasajero = Pasajero.objects.all()
    return render(request, template_name='pasajero/list_pasajero.html', context={'pasajero':pasajero})

class pasajeroForm(ModelForm):
    class Meta:
        model = Pasajero
        fields = [
            'name',
        ]

def create_pasajero(request, template_name = 'pasajero/create_pasajero.html'):
    form = pasajeroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_pasajero')
    return render(request, template_name, {'form': form})

def update_pasajero(request, pk, template_name='pasajero/create_pasajero.html'):
    pasajero_update = get_object_or_404(Nave, pk=pk)
    form = pasajeroForm(request.POST or None, instance=pasajero_update)
    if form.is_valid():
        form.save()
        return redirect('list_pasajero')
    return render(request, template_name, {'form': form})

#BACKEND AERONAVE
def list_aeronave_pasajero(request):
    aeronave_pasajero = Aeronave_Pasajero.objects.all()
    return render(request, template_name='aeronavepasajero/list_aeronave_pasajero.html', context= {'aeronave_pasajero':aeronave_pasajero})

class aeronave_pasajeroForm(ModelForm):
    class Meta:
        model = Aeronave_Pasajero
        fields = [
            'aeronave',
            'pasajero',
        ]

def create_aeronave_pasajero(request, template_name = 'aeronavepasajero/create_aeronave_pasajero.html'):
    form = aeronave_pasajeroForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_aeronave_pasajero')
    return render(request, template_name, {'form': form})

def update_aeronave_pasajero(request, pk, template_name='aeronavepasajero/create_aeronave_pasajero.html'):
    aeronave_pasajero_update = get_object_or_404(Nave, pk=pk)
    form = aeronave_pasajeroForm(request.POST or None, instance=aeronave_pasajero_update)
    if form.is_valid():
        form.save()
        return redirect('list_aeronave_pasajero')
    return render(request, template_name, {'form': form})

#BACKEND REVISION
def list_revision(request):
    revision = Revision.objects.all()
    return render(request, template_name='revision/list_revision.html', context= {'revision':revision})

class revisionForm(ModelForm):
    class Meta:
        model = Revision
        fields = [
            'name',
            'fecha_registra',
            'aeronave',
            #'pasajeros',
        ]

def create_revision(request, template_name = 'revision/create_revision.html'):
    form = revisionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_revision')
    return render(request, template_name, {'form': form})

def update_revision(request, pk, template_name='revision/create_revision.html'):
    revision_update = get_object_or_404(Nave, pk=pk)
    form = revisionForm(request.POST or None, instance=revision_update)
    if form.is_valid():
        form.save()
        return redirect('list_revision')
    return render(request, template_name, {'form': form})