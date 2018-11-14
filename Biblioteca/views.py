from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import *
from Biblioteca import forms
from django.urls import reverse_lazy 

# Create your views here.



def base(request):
    return render(request, 'baseAdmin.html')

def editorial_base(request):
    e = Editorial.objects.all()
    context = {'editorial_list': e}
    return render(request, 'ListaEditorial.html', context)

class EditorialCreate(CreateView):
    model = Editorial
    form_class = forms.EditorialForm
    template_name = 'EditorialCreate.html'
    success_url = reverse_lazy('lista_editorial')

class EditorialEditar(UpdateView):
    model = Editorial
    form_class = forms.EditorialForm
    template_name = 'EditorialEditar.html'
    success_url = reverse_lazy('lista_editorial')

class EditorialDelete(DeleteView):
    model = Editorial
    template_name = 'editorial_confirm_delete.html'
    success_url = reverse_lazy('lista_editorial')