from django.shortcuts import render
from .models import Project

# Create your views here.

def portfolio(request):

    projects = Project.objects.all()

    context = {
        'proyectos': projects
    }

    return render(request, "portfolio/portfolio.html", context)