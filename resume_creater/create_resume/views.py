from django.shortcuts import render,redirect
from .models import ResumeModel
from .forms import DetailForm,ProjectForm

# Create your views here.
def create(request):
    if request.method == 'POST':
        details = DetailForm(request.POST)
        project = ProjectForm(request.POST)
        if details.is_valid() and project.is_valid():
            details.save()
            project.save()
            redirect('resume/resume')
        context = {'details':details,'project':project}
        return render(request,'create.html',context )
    else:
        project = ProjectForm()
        details = DetailForm()
        context = {'details':details,'project':project}
    return render(request,'create.html',context)


def resume(request):
    return render(request,'resume.html')