from django.shortcuts import render
from django.core.mail import send_mail,settings
from django.views import View
from django.http import HttpResponse


# Create your views here.
class EmailsendView(View):
    def get(self,request):
        sub="testing mail send"
        msg="test is successful"
        from_addr=settings.EMAIL_HOST_USER
        to="ananthu.cpt.21@gmail.com"
        res=send_mail(sub,msg,from_addr,[to])
        if res:
            return HttpResponse("mail sent succesfully")
        else:
            return HttpResponse("mail sent unsuccesful")