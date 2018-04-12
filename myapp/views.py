from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Articulo

def like(request,id,accion):
	#pasos para actualizar el like en el modelo Articulo

	#paso 1 Crear Objeto:
	art = Articulo.objects.get(pk=id)

	# Paso 2  editar el objeto:    pueden haber 2 acciones : Like o DisLike

	if accion == "like":
		art.likes += 1
	else:
		art.dislikes += 1

	#paso 3   Guardar cambios del objeto
	art.save()

	return HttpResponseRedirect(reverse('articulo', args=[art.slug]))  #genera automaticamente la url de articulo, luego de dar like, para que vuelva a la pagina del articulo



def index(request):
	#SELECT * FROM Articulos: queryset
	articulos = Articulo.objects.all().order_by("-id") # .order_by("-id") para que ordene de forma descendente

	return render(request, 'index.html',{'articulos':articulos})

def articulo(request,slug):
	art = Articulo.objects.get(slug=slug)   #get es para mostrar un objeto en especifico y filter para filtrar por nombres o cualquier otro dato

	return render(request, 'articulo.html',{'articulo': art})

