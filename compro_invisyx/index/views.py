from django.shortcuts import render, redirect
from django.templatetags.static import static
from .models import *
from django.contrib import messages


def index(request) :
    return render(request, 'index_pages/home.html', {
        'web_title' : "Invisyx".title(),
    })

def contactus(request) :
    if request.method == 'POST' :
        metode = request.POST.get('metode', '')

        if metode == 'post' :
            name = request.POST.get('name-name', '')
            phone = request.POST.get('phone', '')
            email = request.POST.get('email', '')
            company = request.POST.get('company', '')
            subject = request.POST.get('subject', '')
            question = request.POST.get('question', '')

            ContactUs.objects.using('default').create(
                name=name,
                phone_number=phone,
                email=email,
                company=company if company else None,
                subject=subject,
                question=question
            )

            messages.success(request, f"Your email has been delivered, stay tuned at your email for reply.")
            return redirect('index:contactus')

    return render(request, 'index_pages/contactus.html', {
        'web_title' : "Invisyx".title(),
    })