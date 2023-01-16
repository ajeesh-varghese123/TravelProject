from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    #path('opr/',views.operation,name='operation'),
   # path('content/',views.content,name='content')

]



