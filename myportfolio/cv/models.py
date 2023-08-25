from django.db import models
from django.contrib.auth.models import User


class UserCV(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cv")
    bio = models.TextField(blank=True)
    experience = models.TextField(blank=True)
    education = models.TextField(blank=True)
    skills = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
class WorkHistory(models.Model):
    user_cv  = models.ForeignKey(UserCV, on_delete=models.CASCADE, related_name="work_histories")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # If currently working, this might be blank
    position = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f"{self.user_cv} - {self.position}"


class Education(models.Model):
    user_cv = models.ForeignKey(UserCV, on_delete=models.CASCADE, related_name="educations")
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='certificates/')  # You'll need to set up media handling for this

    def __str__(self):
        return f"{self.user_cv} - {self.title}"
    

