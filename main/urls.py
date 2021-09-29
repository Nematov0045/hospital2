from django.urls import path
from django.urls.conf import include
from .views import detail, index, AddDoctors, AddPatient, AddNurse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',index,name='index'),
    path('detail/<int:pk>', detail,name='detail'),
    path('doctor/registration',AddDoctors.as_view(),name='addDoctor'),
    path('nurse/registration',AddNurse.as_view(),name='addnurse'),
    path('patient/registration',AddPatient.as_view(),name='addpatient'),
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)