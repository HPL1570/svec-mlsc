from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'html/index.html')
def team(request):
    return render(request, 'html/teams.html')
def event(request):
    return render(request, 'html/events.html')
def blog(request):
    return render(request, 'html/blogs.html')
def project(request):
    return render(request, 'html/projects.html')