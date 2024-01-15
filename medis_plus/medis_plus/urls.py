from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.Index, name='index'),
                  path('about/', views.About, name='about'),
                  path('doctors/', views.Doctors, name='doctors'),
                  path('services/', views.Services, name='services'),
                  path('contact/', views.Contact, name='contact'),
                  path('appointment/<int:docs_id>', views.Appointments, name='appointment'),
                  path('doctordetail/<int:doc_id>', views.DoctorDetails, name='doctordetails'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
