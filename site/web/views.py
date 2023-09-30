from django.shortcuts import render
from web.models import *

def viewhome(request):
    mentors = Mentor.objects.all()
    logos = Logo.objects.all()
    links = Link.objects.all()
    abouts = About.objects.all()
    stats = Stat.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', {'mentors': mentors, 'logos': logos, 'links': links, 'abouts': abouts, 'stats': stats, 'courses': courses})