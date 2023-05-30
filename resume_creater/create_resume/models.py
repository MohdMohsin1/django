from django.db import models

# Create your models here.
class ResumeModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    DOB = models.DateTimeField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=4)
    contry = models.CharField(max_length=100)
    email = models.EmailField()
    link =models.CharField(max_length=300)

# class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_desc = models.CharField(max_length=100)

# class Education(models.Model):
    college = models.CharField(max_length=100)
    # stream = models.models.CharField( max_length=50)
    degree = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

# class certification(models.Model):
    course_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


# class skills(models.Model):
    skill = models.CharField(max_length=50)

    
# class hobbies(models.Model):
    hobby = models.CharField(max_length=50)

    
# class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    Experience = models.CharField(max_length=10)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    


