from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Company, Project

# Create your views here.

def landing(request):
    
    company = Company.objects.all()
    
    context ={
        "company":company
    }
    
    if request.method == 'POST':
        
        name = request.POST['name']
        email = request.POST['email']
        company = request.POST['company']
        subject = request.POST['subject']
        message = request.POST['message']
        
        
        html = render_to_string('base/contactUs.html', {
            'name':name,
            'email':email,
            'company':company,
            'subject':subject,
            'message':message,
        })

            # Send welcome email
        subject = name
        message = message
        from_email = email
        to_email = ['prosperbiz720@gmail.com']
        send_mail(subject, message, from_email, to_email, html_message=html, fail_silently=False)
        # messages.success(request, 'we have seen the message')
        return redirect('home')
    
    return render(request, "base/landing.html", context)

def company_page(request, slug):
    
    category = get_object_or_404(Company, slug=slug)
    
    projects = Project.objects.filter(category=category)
    
    context = {
        
        'projects':projects,
        'category':category
        
    }
    
    return render(request, 'base/company_page.html', context)