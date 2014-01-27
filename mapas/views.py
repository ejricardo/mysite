from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
import pygmaps
# from lib import pygmaps

# Create your views here.
def index(request):	
	mymap = pygmaps.maps(20.680329,-103.348732,17)
	mapa = mymap.script_drawmap() 
	miubicacion = mymap.script_self_point()
	c = Context({'drawselfpoint':miubicacion,'drawmap':mapa})
	t = get_template("mimapa.html")
	html = t.render(c)
	return HttpResponse(html) 


 
def mapa(request, x,y):
	dt="hola" + x +" y " + y
	return HttpResponse(dt)


def busca(request, x,y, buscar):
	dt="hola" + x +" y " + y + "buscas : "+buscar
	return HttpResponse(dt)