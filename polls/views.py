
from django.shortcuts import render
from .models import jadval, phone
from django.http import JsonResponse
from .serializer import jadvalSerializer, phoneSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# def all(request):
#     all=jadval.objects.all()
#     result=jadvalSerializer(all, many=True)
#     # for i in all:
#     #     mylist.append({
#     #         'name':i.name,
#     #         'nechtaligi':i.nechtaligi
#     #     })
# #     return JsonResponse(result.data, safe=False)
# class getjadval(APIView):
#     def get(self, request):
#         choose = jadval.objects.all()
#         yeah=jadvalSerializer(choose, many=True)
#         return Response(yeah.data)
class GetAllJadval(generics.ListAPIView):
    queryset=jadval.objects.all()
    serializer_class=jadvalSerializer
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return jadval.objects.all()




class GetDetailJadval(generics.RetrieveAPIView):
    queryset = jadval.objects.all()
    serializer_class=jadvalSerializer
    # class getjadval(APIView):
#     def get(self, request):
#         choose = jadval.objects.all()
#         yeah=jadvalSerializer(choose, many=True)
#         return Response(yeah.data)

class PostJadval(generics.CreateAPIView):
    queryset=jadval.objects.all()
    serializer_class=jadvalSerializer




class PatchJadval(generics.UpdateAPIView):
    queryset=jadval.objects.all()
    serializer_class=jadvalSerializer

class DeleteJadval(generics.DestroyAPIView):
    queryset=jadval.objects.all()
    serializer_class=jadvalSerializer


    

# def detail(request, myid):
#     # each = phone.objects.get(id=myid)
#     # data={'name':each.name, 'number':each.number}
#     some = phone.objects.filter(id=myid)
#     forgett = phoneSerializer(some, many=True)
#     return JsonResponse(forgett.data, safe=False)

class PostGetJadval(generics.ListCreateAPIView):
    queryset=jadval.objects.all()
    serializer_class=jadvalSerializer

class AllFunctionJadval(generics.RetrieveUpdateDestroyAPIView):
    queryset=jadval.objects.all()
    serializer_class=jadvalSerializer


    


# def detail(request, myid):
#     # each = phone.objects.get(id=myid)
#     # data={'name':each.name, 'number':each.number}
#     some = phone.objects.filter(id=myid)
#     forgett = phoneSerializer(some, many=True)
#     return JsonResponse(forgett.data, safe=False)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class GetAllPhone(generics.ListAPIView):
    queryset=phone.objects.all()
    serializer_class=phoneSerializer
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return phone.objects.all()



class GetDetailPhone(generics.RetrieveAPIView):
    queryset = phone.objects.all()
    serializer_class=phoneSerializer

class PostPhone(generics.CreateAPIView):
    queryset=phone.objects.all()
    serializer_class=phoneSerializer
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



class PatchPhone(generics.UpdateAPIView):
    queryset=phone.objects.all()
    serializer_class=phoneSerializer

class DeletePhone(generics.DestroyAPIView):
    queryset=phone.objects.all()
    serializer_class=phoneSerializer

    
# class postjadval(APIView):
#     def post(self, request):
#         boldi=request.data
#         serious = jadvalSerializer(data=boldi)
#         if serious.is_valid():
#             serious.save()
#             return Response(serious.data)
#         return Response(serious.errors)

class PostGetPhone(generics.ListCreateAPIView):
    queryset=phone.objects.all()
    serializer_class=phoneSerializer



class AllFunctionPhone(generics.RetrieveUpdateDestroyAPIView):
    queryset=phone.objects.all()
    serializer_class=phoneSerializer


# class postjadval(APIView):
#     def post(self, request):
#         boldi=request.data
#         serious = jadvalSerializer(data=boldi)
#         if serious.is_valid():
#             serious.save()
#             return Response(serious.data)
#         return Response(serious.errors)
        
