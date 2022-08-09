from django.shortcuts import render
from django.http import JsonResponse
from .models import NewData
from django.core import serializers
from django.views.decorators import csrf
import json
# Create your views here.

def get_data(request):
    res={
        'name':'chiranth',
        'email':'chiranth@appinessworld.com',
        'status':'OK success'
    }
    return JsonResponse(res)

def post_data(request):
    if request.method == 'POST':
        res={
            'name': 'chiranth',
            'email': 'chiranth@appinessworld.com',
            'status': 'OK success'
        }
    else:
        res={
            'status': 'wrong path'
        }
    return JsonResponse(res)

def TheModelView(request):
    if(request.method=='GET'):
        data=serializers.serialize('json',NewData.objects.all())
        return JsonResponse(json.loads(data),safe=False)

def newdata(request):
    data = list(NewData.objects.values())
    return JsonResponse(data,safe=False)
# def get(self, request):
#         friend_list = list(MyFriendList.objects.values())
#         return JsonResponse(friend_list, safe=False)
