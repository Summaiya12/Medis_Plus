from django.shortcuts import render
from .models import DoctorDetail, Category, Appointment, Contacts


def Index(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def Doctors(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'doctor.html', context)


def Services(request):
    return render(request, 'services.html')


def Contact(request):
    if request.method == 'POST':
        # Handle form submission
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        contact_message = Contacts.objects.create(name=name, email=email, message=message, subject=subject, phone=phone)
        contact_message.save()
    return render(request, 'contact.html')


def Appointments(request, docs_id):
    app = DoctorDetail.objects.filter(id=docs_id)
    context = {
        "app": app

    }
    if request.method == 'POST':
        appoint = Appointment()
        aname = request.POST.get('name')
        aemail = request.POST.get('email')
        aphone = request.POST.get('phone')
        adate = request.POST.get('date')
        amessage = request.POST.get('doctor')
        appoint.name = aname
        appoint.email = aemail
        appoint.phone = aphone
        appoint.date = adate
        appoint.doctor = amessage
        appoint.save()
        return render(request, 'new.html')
    return render(request, 'appointment.html', context)


def DoctorDetails(request, doc_id):
    categories = Category.objects.get(id=doc_id)
    detail = DoctorDetail.objects.filter(category=categories)
    doctor = DoctorDetail.objects.all()
    context = {
        "categories": categories,
        "detail": detail,
        "doctor": doctor

    }
    return render(request, 'doctordetail.html', context)
