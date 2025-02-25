from django.db import models

class Evaluation(models.Model):
    description = models.TextField()
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Foreign Keys
    candidate = models.ForeignKey('candidates.Candidate', on_delete=models.CASCADE)
    vacancy = models.ForeignKey('vacancies.Vacancy', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.candidate} - {str(self.score)}"
