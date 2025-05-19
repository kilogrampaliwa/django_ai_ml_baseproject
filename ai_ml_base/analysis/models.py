from django.db import models

# Create your models here.

#____________________________________________________
# Logic:
# AnalysisInput: Django website -> some ML stuff
# AnalysisResult: ML stuff -> Django website
#____________________________________________________

class AnalysisInput(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/', blank=True, null=True)
    raw_text = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=50, choices=[
        ('cv', 'CV'),                   # - a program for resume consultation
        ('flight', 'Flight Data'),      # - engineering/pilot's app for flight data analysis
        ('finance', 'Finance'),         # - simple app for home budget analysis
        ('wing', 'Wing Design'),        # - engineering program for wing design
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AnalysisResult(models.Model):
    analysis_input = models.ForeignKey(AnalysisInput, on_delete=models.CASCADE)
    result_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.analysis_input.name}"
