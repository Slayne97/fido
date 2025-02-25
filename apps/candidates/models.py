from django.db import models

# Create your models here.


class Candidate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    resume = models.FileField(upload_to="resumes/", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name
