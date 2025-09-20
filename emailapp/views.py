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
        
class MailSend(View):
    def get(self,request):
        return render(request,"mailform.html")
    
    def post(self,request):
        sub=request.POST.get("subject")
        msg=request.POST.get("msg")
        mailid=request.POST.get("mailid")
        res=send_mail(sub,msg,settings.EMAIL_HOST_USER,[mailid])
        if res:
            return HttpResponse("mail succesfull")
        else:
            return HttpResponse("mail not succesfull")

        