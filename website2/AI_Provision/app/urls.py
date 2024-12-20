from django.urls import path
from . import views


urlpatterns = [
    
    path("",views.index,name='home' ),
    path("home",views.index,name='home' ),
    path("plateform",views.plateform,name='plateform' ),
    path("resources",views.resources,name='resources' ),
    path("prizing",views.prizing,name='prizing' ),
    path("solution",views.solution,name='solution' ),
    path("company",views.company,name='company' ),
    
]