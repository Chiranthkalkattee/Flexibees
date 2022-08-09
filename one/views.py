from django.shortcuts import render
from .models import Candidate_feedback_report
from .serializers import Serializers
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import csv
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import SendMailForm
from django.views import View
# Create your views here.

def Candidate_report(request):
    if request.method == 'POST':
        # if request.Candidate_feedback_report.get('Client_name') and request.Candidate_feedback_report.get('Roles') and request.Candidate_feedback_report.get('BD_manager') and request.Candidate_feedback_report.get('Recruiter') and request.Candidate_feedback_report.get('candidate_name') and request.Candidate_feedback_report.get('selection'):
            post = Candidate_feedback_report()
            post.Client_name = request.POST.get('Client_name')
            post.Roles = request.POST.get('Roles')
            post.BD_manager = request.POST.get('BD_manager')
            post.Recruiter = request.POST.get('Recruiter')
            post.candidate_name= request.POST.get('candidate_name')
            post.selection= request.POST.get('selection')
            post.save()

            return render(request, 'Candidate_feedback.html')

    else:
        return render(request, 'Candidate_feedback.html')


#     Client_name = request.POST["Client_name"]
#     Roles = request.POST["Role"]
#     BD_manager = request.POST["BD_manager"]
#     Recruiter = request.POST["Recruiter"]
#     candidate_name = request.POST["candidate_name"]
#     selection = request.POST["selection"]
#     candidate = Candidate_feedback_report(Client_name=Client_name,Roles=Roles,BD_manager=BD_manager,Recruiter=Recruiter,candidate_name=candidate_name,selection=selection)
#     candidate.save()
#     return render(request,'candidate_feedback.html')

#     if request.method == "POST":
#         form = MyForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse({MyForm})
#         else:
#             return HttpResponse("<h1>wrong password</h1>")
#     else:
#         form = MyForm()
#     print('hello')
#     return render(request,'Candidate_feedback.html'),


def Candidate_list(request):
    if request.method =='GET':
        data = Candidate_feedback_report.objects.all()
        serializer = Serializers(data,many=True)
        return JsonResponse(serializer.data,safe=False)

def export_to_csv(request):
    Candidate = Candidate_feedback_report.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=candidate_feedback_report.csv'
    write =csv.writer(response)
    write.writerow(['Client_name','Roles','BD_manager','Recruiter','candidate_name','selection'])
    fields=Candidate.values_list("Client_name","Roles","BD_manager","Recruiter","candidate_name","selection")
    for candidate in fields:
        write.writerow(candidate)
    return response


def simple_send_mail(request):
    if request.method == 'POST':
        fm = SendMailForm(request.POST or None, request.FILES or None)
        if fm.is_valid():
            subject = fm.cleaned_data['subject']
            message = fm.cleaned_data['msg']
            from_mail = request.user.email
            to_mail = fm.cleaned_data['email_id']
            to_cc = fm.cleaned_data['email_cc']
            to_bcc = fm.cleaned_data['email_bcc']
            attach = fm.cleaned_data['attachment']
            if from_mail and to_mail:
                try:
                    mail = EmailMessage(subject=subject, body=message, from_email=from_mail, to=[to_mail], bcc=[to_bcc],
                                        cc=[to_cc]
                                        )
                    mail.attach(attach.name, attach.read(), attach.content_type)
                    mail.send()
                # except Exception as ex:
                except ArithmeticError as aex:
                    print(aex.args)
                    return HttpResponse('Invalid header found')
                return HttpResponseRedirect('/mail/thanks/')
            else:
                return HttpResponse('Make sure all fields are entered and valid.')
    else:
        fm = SendMailForm()
    return render(request, 'mailattachment.html', {'fm': fm})


def thank_you(request):
    return render(request,'thankyou.html')