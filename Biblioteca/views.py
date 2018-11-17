from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import *
from Biblioteca import forms
from django.urls import reverse_lazy 

# Create your views here.


#Vistas para el CRUD de Editoriales
def base(request):
    return render(request, 'baseAdmin.html')

def editorial_base(request):
    e = Editorial.objects.all()
    context = {'editorial_list': e}
    return render(request, 'ListaEditorial.html', context)

def libros_editorial(request, pk):
    libros = Editorial.objects.get(id=pk)
    context = {'object': libros}
    return render(request, 'listaLibrosPorEditorial.html', context)

class EditorialCreate(CreateView):
    e = Libro.objects.all()
    context = {'libro_list': e}
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

# Vistas para el CRUD de libros

def libro_base(request):
    e = Libro.objects.all()
    context = {'libro_list': e}
    return render(request, 'ListaLibro.html', context)

class LibroCreate(CreateView):
    model = Libro
    form_class = forms.LibroForm
    template_name = 'LibroCreate.html'
    success_url = reverse_lazy('lista_libro')

class LibroEditar(UpdateView):
    model = Libro
    form_class = forms.LibroForm
    template_name = 'LibroEditar.html'
    success_url = reverse_lazy('lista_libro')

class LibroDelete(DeleteView):
    model = Libro
    template_name = 'Libro_confirm_delete.html'
    success_url = reverse_lazy('lista_libro')