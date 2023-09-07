
from django.shortcuts import render
from .models import jadval, phone
from django.http import JsonResponse
from .serializer import jadvalSerializer, phoneSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

# def all(request):
#     all=jadval.objects.all()
#     result=jadvalSerializer(all, many=True)
#     # for i in all:
#     #     mylist.append({
#     #         'name':i.name,
#     #         'nechtaligi':i.nechtaligi
#     #     })
#     return JsonResponse(result.data, safe=False)
class getjadval(APIView):
    def get(self, request):
        choose = jadval.objects.all()
        yeah=jadvalSerializer(choose, many=True)
        return Response(yeah.data)
    


def detail(request, myid):
    # each = phone.objects.get(id=myid)
    # data={'name':each.name, 'number':each.number}
    some = phone.objects.filter(id=myid)
    forgett = phoneSerializer(some, many=True)
    return JsonResponse(forgett.data, safe=False)


class postjadval(APIView):
    def post(self, request):
        boldi=request.data
        serious = jadvalSerializer(data=boldi)
        if serious.is_valid():
            serious.save()
            return Response(serious.data)
        return Response(serious.errors)
        
