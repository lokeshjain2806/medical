from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def feature(request):
    return render(request, 'feature.html')

def doctors(request):
    return render(request, 'team.html')

def appointment(request):
    return render(request, 'appointment.html')

def feedback(request):
    return render(request, 'testimonial.html')