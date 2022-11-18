from django.shortcuts import render
from .models import Usuario
from django.http.response import JsonResponse

# Create your views here.
class UsuarioView(View):
    
    def get(self,request):
        if (id > 0):
            usuarios = list(Usuario.objects.filter(id=id).values())
            if len(usuarios) > 0:
                company = usuarios[0]
                datos = {'message': "Success", 'company': company}
            else:
                datos = {'message': "Usuarios no encontrados..."}
            return JsonResponse(datos)
        else:
            usuarios = list(Usuario.objects.values())
            if len(usuarios) > 0:
                datos = {'message': "Success", 'companies': companies}
            else:
                datos = {'message': "Usuarios no encontrados..."}
            return JsonResponse(datos)
    
    def post(self,request):
        pass

    def put(self,request):
        pass
    
    def delete(self,request):
        pass
