from django import forms
from .models import ResumeModel



class DetailForm(forms.ModelForm):
    # ResumeModel fields
    class Meta:
        model = ResumeModel
        fields = ['first_name','last_name','DOB','address', 'city','state','contry', 'email','link']

class ProjectForm(forms.ModelForm):
    class Meta:
        model =ResumeModel
        fields = ['project_name','project_desc']