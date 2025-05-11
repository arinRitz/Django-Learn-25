
from django.urls import path
from . import views
#localhost:8080/chai
urlpatterns = [
   
    path('',views.all_chai, name='all_chai'),
   
]
