from django.shortcuts import render
from .models import Employee_details
from django.http import HttpResponse,response
import csv







def export_to_csv(request):
    Candidate = Employee_details.objects.all()
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=Employee_details_report.csv'
    write =csv.writer(response)
    write.writerow(['Employee_name','Phone_number','Email','Designation'])
    fields=Candidate.values_list("Employee_name","Phone_number","Email","Designation")
    for candidate in fields:
        write.writerow(candidate)
    return response











# # from django.core.files import File
# from django.http import HttpResponse
# # import docx
# from django.http import FileResponse
# import os
# from PyPDF2 import PdfReader


# # Create your views here.


# def readfile(request):
#     filepath = os.path.join('Poorvi.pdf')
#     print(filepath);
#     return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
#     return HttpResponse();



# def newfilereader(request):
#     reader = PdfReader("Anubhav.pdf")
#     number_of_pages = len(reader.pages)
#     page = reader.pages[0]
#     text =str(page.extract_text())
#     print(text.encode('utf-8'))
#     Technical_skills=text[792:1150]
#     return HttpResponse(Technical_skills);