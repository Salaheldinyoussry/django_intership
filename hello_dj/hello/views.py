from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse 
from .models import *
from django.core.mail import send_mail
# Create your views here.
   
   
def home(request):   
   
   return render(request , 'hello/home.html')
  
def secondPage(request): 
  ca=company.objects.all().order_by('name').distinct()

 
  c1=company.objects.filter(cm1='1')
  c2=company.objects.filter(cm2='1')
  c3=company.objects.filter(cm3='1')
  c12=company.objects.filter(cm1='1')&company.objects.filter(cm2='1')
  #company.objects.filter(Q(ountry=1) | Q(country=2))
  c13=company.objects.filter(cm1='1')&company.objects.filter(cm3='1')
  #company.objects.filter(Q(country=1) | Q(country=3))
  c23=company.objects.filter(cm2='1')&company.objects.filter(cm3='1')
  #company.objects.filter(Q(country=2) | Q(country=3))

  contex={'ca':ca ,'c1':c1 ,'c2':c2 ,'c3':c3 ,'c12':c12 ,'c13':c13 ,'c23':c23 }
  #send_mail('hello','try this','djangoprojectservice@gmail.com',['yatow42740@wedbo.net'])



  return render(request , 'hello/secondPage.html',contex)

def thirdPage(request):   
   
   return render(request , 'hello/thirdPage.html')




def appointment(request):
   print(request.POST['newCompany']) 
   #lname=request.POST['lname']
   #fname=request.POST['fname']
   # cont=request.POST['country']
   # #z=str(lname)+str(fname)
   # print(cont) 
   #country=request.POST['company']
   # country=request.POST.get('company')
   # if(str(country)=='choose company'):
   #      print("ko")
   #      country=request.POST['company1'] 
   #      if(str(country)=='choose company'):
   #          country=request.POST['company2'] 
   #          if(str(country)=='choose company'):
   #              country=request.POST['company3'] 
   #              if(str(country)=='choose company'):
   #                   country=request.POST['company4'] 
   #                   if(str(country)=='choose company'):
   #                      country=request.POST['company5'] 
   #                      if(str(country)=='choose company'):
   #                         country=request.POST['company6'] 
       

   return render(request , 'hello/thirdPage.html')

 ##

# send email with form data as string
 ###

    
   # fname=request.POST.get('scountry')
   #fname=request.cleaned_data['scountry']


  

