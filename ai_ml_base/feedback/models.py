from django.db import models
from analysis.models import AnalysisInput

# Create your models here.

#____________________________________________________
# Logic:
# Feedback: Django website -> user feedback
#____________________________________________________

class Feedback(models.Model):
    analysis_input = models.ForeignKey(AnalysisInput, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.analysis_input.name}"
