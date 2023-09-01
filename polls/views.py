
from django.shortcuts import render
from .models import jadval, phone
from django.http import JsonResponse
from .serializer import jadvalSerializer, phoneSerializer

# Create your views here.

def all(request):
    all=jadval.objects.all()
    result=jadvalSerializer(all, many=True)
    # for i in all:
    #     mylist.append({
    #         'name':i.name,
    #         'nechtaligi':i.nechtaligi
    #     })
    return JsonResponse(result.data, safe=False)
    


def detail(request, myid):
    # each = phone.objects.get(id=myid)
    # data={'name':each.name, 'number':each.number}
    some = phone.objects.filter(id=myid)
    forgett = phoneSerializer(some, many=True)
    return JsonResponse(forgett.data, safe=False)
        
