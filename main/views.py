from django.shortcuts import render
from .models import Hospital, MainDoctor,Doctor,Patient
from django.views.generic import CreateView
from .forms import *
# Create your views here.
def index(request):
    hospitals=Hospital.objects.all()
    return render(request,'index.html',{'hospitals':Hospital.objects.all()})
def detail(request,pk):
    hospital_detail = Hospital.objects.get(pk=pk)
    maindoctor_detail = Doctor.objects.filter(hospital=pk)
    patients_detail=Patient.objects.filter(doctor=pk)
    context = {
        'hospital_detail':hospital_detail,
        'maindoctor_detail':maindoctor_detail,
        'patient_detail':patients_detail,}
    return render(request,"detail.html",context)
class  AddDoctors(CreateView):
    form_class = AddDoctor
    template_name ='addnew.html'
    raise_exception = True
class  AddNurse(CreateView):
    form_class = AddNurses
    template_name ='addnew.html'
    raise_exception = True
class  AddPatient(CreateView):
    form_class = AddPatient
    template_name ='addnew.html'
    raise_exception = True