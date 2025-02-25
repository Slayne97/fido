from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.FloatField()
    company = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
