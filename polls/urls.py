from django.urls import path
from .views import (GetAllJadval, 
                    PostJadval, 
                    GetDetailJadval,
                      PatchJadval, 
                      DeleteJadval,
                        AllFunctionJadval,
                          PostGetJadval)



from .views import ( GetAllPhone, 
                    GetDetailPhone, 
                    PostPhone,
                     PatchPhone,
                     DeletePhone,
                     AllFunctionPhone, 
                    PostGetPhone)

urlpatterns=[
    path('GetAllJadval/', GetAllJadval.as_view()),
    path('GetDetailJadval/<int:pk>', GetDetailJadval.as_view()),
    path('PostJadval/', PostJadval.as_view() ),
    path('PatchJadval/<int:pk>', PatchJadval.as_view()),
    path('DeleteJadval/<int:pk>', DeleteJadval.as_view()),
    path('PostGetJadval/', PostGetJadval.as_view()),
    path('AllFunctionJadval/<int:pk>', AllFunctionJadval.as_view()),
    path('GetAllPhone/', GetAllPhone.as_view()),
    path('GetDetailPhone/<int:pk>', GetDetailPhone.as_view()),
    path('PostPhone/', PostPhone.as_view() ),
    path('PatchPhone/<int:pk>', PatchPhone.as_view()),
    path('DeletePhone/<int:pk>', DeletePhone.as_view()),
    path('PostGetPhone/', PostGetPhone.as_view()),
    path('AllFunctionPhone/<int:pk>', AllFunctionPhone.as_view())


]