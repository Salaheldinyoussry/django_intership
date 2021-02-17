from django.urls import path
from . import views    


urlpatterns = [
    path('' ,views.home , name="home"),
    path('secondPage' ,views.secondPage, name="secondPage"),
    path('thirdPage' ,views.thirdPage, name="thirdPage"),
    path('appointment' ,views.appointment, name="appointment"),

   # path('ajax/load-cm/', views.load_cm, name='ajax_load_cm'), # AJAX


]