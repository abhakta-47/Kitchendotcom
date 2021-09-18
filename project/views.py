from django.shortcuts import get_object_or_404, render
from project.models import Project, PostImage, Video, Design, Feedback

# Create your views here.
def projectList(request):
    video = Video.objects.all()
    design = Design.objects.all()
    feedback = Feedback.objects.all()
    projects = Project.objects.all()
    for project in projects:
        print(project)
    return render( request, "project_gallery.html", {
        'project':projects, 
        'video':video, 
        'design':design, 
        'feedback':feedback
        })
 
def projectDetails(request, id):
    project = get_object_or_404(Project, id=id)
    print(project.name)
    photos = PostImage.objects.filter(project=project)
    return render(request, 'project_details.html', {
        'project':project,
        'photos':photos
    })


# def projectDetails(request, projectId):
#     try:
#         context = {}
#         __project = Project.objects.get(id=projectId)
#         # __project = Project.objects.filter(Project=__project)
#         context = {'project': __project}
#     # __project = 
#         print(__project)
#         return render( request, "project_details.html", context)
#     except:
#         print("not found")
#         return render( request, "project_details.html")
# def projectList(request):
#     posts = Project.objects.all()
#     return render(request, 'project_gallery.html', {'posts':posts})