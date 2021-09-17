from django.shortcuts import render
from project.models import Project

# Create your views here.
def projectList(request):
    projects = Project.objects.all()
    for project in projects:
        print(project)
    return render( request, "project_gallery.html", {project:projects})

def projectDetails(request, projectId):
    try:
        context = {}
        __project = Project.objects.get(id=projectId)
        # __project = Project.objects.filter(Project=__project)
        context = {'project': __project}
    # __project = 
        print(__project)
        return render( request, "project_details.html", context)
    except:
        print("not found")
        return render( request, "project_details.html")