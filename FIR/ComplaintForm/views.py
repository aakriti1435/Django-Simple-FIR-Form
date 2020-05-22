from django.shortcuts import render
from django.http import HttpResponse
from .models import InputForm


# Create your views here.
def complaintform(request):
    if request.POST:
        print(request)
        first_name = request.POST.get('first_name','')
        print(first_name)
        last_name = request.POST.get('last_name','')
        father_husband_name = request.POST.get('father_husband_name','')
        email = request.POST.get('email','')
        mobile = request.POST.get('mobile','')
        address1 = request.POST.get('address1','')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip_code = request.POST.get('zip_code','')
        distance = request.POST.get('distance','')
        direction = request.POST.get('direction','')
        date = request.POST.get('date','')
        time = request.POST.get('time','')
        nature_offence = request.POST.get('nature_offence','')
        particulars_property = request.POST.get('particulars_property','')
        description_accused = request.POST.get('description_accused','')
        witness_details = request.POST.get('witness_details','')
        brief_facts = request.POST.get('brief_facts','')
        
        input = InputForm(first_name=first_name, last_name=last_name, father_husband_name=father_husband_name, email=email, mobile=mobile, address1=address1, address2=address2, city=city, state=state, zip_code=zip_code, distance=distance, direction=direction, date=date, time=time, nature_offence=nature_offence, particulars_property=particulars_property, description_accused=description_accused, witness_details=witness_details, brief_facts=brief_facts)
        input.save()


    return render(request, 'complaintform.html') 


def formsubmitted(request):
    #return HttpResponse('Form submitted successfully !')
    return render(request, 'formsubmitted.html')