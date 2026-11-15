from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from crm.models import Player
from json import loads
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(csrf_exempt,name="dispatch")
class PlayerListCreateView(View):
  def get(self,request):
    qs=Player.objects.all().values()
    response_data=list(qs)
    return JsonResponse(response_data,safe=False)
  
  def post(self,request):
    json_data=request.body
    form_data=loads(json_data)
    Player.objects.create(**form_data)
    response_data={"message":"record added..."}
    return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")
class PlayerRetrieveUpdateDeleteView(View):
  def get(self,request,pk=None):
    qs=Player.objects.filter(id=pk).values()
    response_data=list(qs)
    return JsonResponse(response_data,safe=False)
  
  def put(self,request,pk=None):
    json_data=request.body
    form_data=loads(json_data)
    Player.objects.update(**form_data)
    response_data={"message":"record updated...."}
    return JsonResponse(response_data)
  
  def delete(self,request,pk=None):
    Player.objects.filter(id=pk).delete()
    response_data={"message":"record deleted ....."}
    return JsonResponse(response_data)