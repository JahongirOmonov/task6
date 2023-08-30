
from django.shortcuts import render
from .models import jadval, phone
from django.http import JsonResponse

# Create your views here.

def all(request):
    all=jadval.objects.all()
    mylist =[]
    for i in all:
        mylist.append({
            'name':i.name,
            'nechtaligi':i.nechtaligi
        })
    return JsonResponse(mylist, safe=False)
    


def detail(request, myid):
    each = phone.objects.get(id=myid)
    data={'name':each.name, 'number':each.number}
    return JsonResponse(data, safe=False)
        
