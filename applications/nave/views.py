from django.shortcuts import render
#from django.http import  HttpResponse
from .models import Naves

# Create your views here.
def NaveView(request):
    nave = Naves.objects.all()
    return  render(request,'listaNave.html')