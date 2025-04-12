from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Project, Skill, MyInfo, Experience, ContactMessage
from .forms import ContactForm

def home(request):
    # Fetch all necessary data for the home page
    profile = Profile.objects.first()  # Assuming there's only one profile
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all().order_by('-start_date')  # Most recent first
    my_info = MyInfo.objects.first()  # Assuming there's only one info record

    # Handle contact form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('home')
    else:
        form = ContactForm()

    # Prepare context for template rendering
    context = {
        'profile': profile,
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
        'my_info': my_info,
        'form': form,
    }
    
    return render(request, 'home.html', context)