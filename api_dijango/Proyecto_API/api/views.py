# from django.shortcuts import render //Renderiza plantillas
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Persona
import json
# Create your views here.

class PersonaView(View):

    #Con esta linea salta  csrf
    @method_decorator(csrf_exempt)
    #Este metodo se ejcuta cuando hacemos una peticion
    def dispatch(self, request,*args,**kwargs):
        return super().dispatch(request, *args, **kwargs)
    #Listamos todas las companias
    def get(self,request,id=0):
        if(id>0):
            #Filtrar por id Persona
            personas=list(Persona.objects.filter(id=id).values())
            if len(personas)>0:
                persona=personas[0]
                datos={'message':"Success",'code':"200",'persona':persona}
            else:
                datos={'message':"Persona not found ..."}
            return JsonResponse(datos)
        else:
            personas=list(Persona.objects.values())
            if len(personas)>0:
                datos={'message':"Success",'code':"200",'personas':personas}
            else:
                datos={'message':"Personas not found ..."}
            return JsonResponse(datos)
        
    #Crear Persona
    def post(self,request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Persona.objects.create(tipodocumento=jd['tipodocumento'],documento=jd['documento'],
        nombres=jd['nombres'],apellidos=jd['apellidos'],hobbie=jd['hobbie'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    #Actualizar Persona

    def put(self,request,id):
        jd=json.loads(request.body)
        personas=list(Persona.objects.filter(id=id).values())
        if len(personas)>0:
            persona=Persona.objects.get(id=id)
            persona.tipodocumento=jd['tipodocumento']
            persona.documento=jd['documento']
            persona.nombres=jd['nombres']
            persona.apellidos=jd['apellidos']
            persona.hobbie=jd['hobbie']
            persona.save()
            datos = {'message': "Success"}
        else:
            datos={'message':"Persona not found ..."}
        return JsonResponse(datos)

    def delete(self,request,id):
        personas=list(Persona.objects.filter(id=id).values())
        if len(personas)>0:
            Persona.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos={'message':"Persona not found ..."}
        return JsonResponse(datos)

