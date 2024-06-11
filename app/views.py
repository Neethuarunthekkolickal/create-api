from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from . serializer import AddressSerializers
from . models import Data
from rest_framework.decorators import api_view

@api_view(["GET","POST","PUT"])
def index(request):
    if request.method=='GET':
        address=Data.objects.all()
        ser=AddressSerializers(address, many=True)
        return JsonResponse(ser.data, safe=False)
    elif request.method=='POST':
        ser=AddressSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, safe=False)
    if request.method=='PUT':
        ser=AddressSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
        return JsonResponse(ser.data, safe=False)
    return JsonResponse() 
@api_view(["GET","DELETE"])
def detail(request,id):
    try:
        address=Data.objects.get(pk=id)
    except Data.DoesNotExist:
        return JsonResponse({'Error':'Data not found'}, status=404)
    if request.method=='GET':
        serilaizer=AddressSerializers(address)
        return JsonResponse(serilaizer.data)
    if request.method=='DELETE':
        address.delete()
        return JsonResponse({'Deleted':'Address Deleted'}, status=204)

     
