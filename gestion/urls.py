from django.conf.urls import url
from django.contrib import  admin 

from . import views
urlpatterns = [
    url(r'^$', 'gestion.views.listar'),
    url(r'^NuevoEstudiante/$', 'gestion.views.NuevoEstudiante'),
    url(r'^NuevaMateria/$', 'gestion.views.NuevaMateria'),
    url(r'^ModificarEstudiante/$', 'gestion.views.ModificarEstudiante'),
    url(r'^ModificarMateria/$', 'gestion.views.ModificarMateria'),
    url(r'^EliminarEstudiante/$', 'gestion.views.EliminarEstudiante'),
    url(r'^EliminarMateria/$', 'gestion.views.EliminarMateria'),
    
]


