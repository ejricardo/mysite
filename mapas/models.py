from django.db import models


class Mapa(models.Model):
	mapa = models.CharField(max_length = 20)
	def __unicode__(self):
		return self.mapa

class Ubicacion(models.Model):
	lat = models.CharField(max_length = 20)
	lon = models.CharField(max_length = 20)
	fecha = models.DateField(auto_now = True)

	def __unicode__(self):
		return self.mapa

class Categoria(models.Model):
	nombreCategoria=models.CharField(max_length = 250)
	def __unicode__(self):
		return self.nombreCategoria

class Negocio(models.Model):
	nombre_negocio = models.CharField(max_length = 250)
	logo = models.ImageField(upload_to='logos', blank = True)
	categoria = models.ForeignKey(Categoria)
	def __unicode__(self):
		return self.nombre_negocio 

class Lugar(models.Model):
	fecha_chk = models.DateField(auto_now = True)
	ubicacion = models.OneToOneField(Ubicacion)
	mapa = models.ForeignKey(Mapa)
	negocio = models.ForeignKey(Negocio)
	def __unicode__(self):
		return self.mapa+self.ubicacion+self.negocio

class Usuario (models.Model):
	usuario = models.CharField(max_length = 250)
	nombre = models.CharField(max_length = 250)
	apellido_materno = models.CharField(max_length = 250)
	apellido_paterno = models.CharField(max_length = 250)
	email = models.CharField(max_length = 250)
	fb = models.CharField(max_length = 250)
	tw = models.CharField(max_length = 250)
	lugar = models.ForeignKey(Lugar)
	def __unicode__(self):
		return self.nombre +' '+ self.apellido_paterno +' '+ self.apellido_materno

		