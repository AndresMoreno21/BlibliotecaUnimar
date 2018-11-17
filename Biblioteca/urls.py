from django.contrib import admin
from django.urls import path, include
from Biblioteca import views

urlpatterns = [
	
    
	path('',views.base,name='base'),
    path('ListaEditorial/',views.editorial_base,name='lista_editorial'),
    path('crearEditorial/',views.EditorialCreate.as_view(),name='editorial_create'),
    path('EditarEditorial/<int:pk>/est',views.EditorialEditar.as_view(),name='editorial_editar'),
    path('BorrarEditorial/<int:pk>/est',views.EditorialDelete.as_view(),name='editorial_borrar'),

    path('ListaLibro/',views.libro_base,name='lista_libro'),
    path('crearLibro/',views.LibroCreate.as_view(),name='libro_create'),
    path('EditarLibro/<int:pk>/est',views.LibroEditar.as_view(),name='libro_editar'),
    path('BorrarLibro/<int:pk>/est',views.LibroDelete.as_view(),name='libro_borrar'),

    path('ListaLibroEditorial//<int:pk>/lbed',views.libros_editorial,name='lista_libro_editorial'),
]