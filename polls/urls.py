from django.urls import path
from .views import getjadval, postjadval, detail

urlpatterns=[
    path('all/', getjadval.as_view()),
    path('detail/<int:myid>', detail),
    path('create/>', postjadval.as_view())
]