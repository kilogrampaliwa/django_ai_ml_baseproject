from django.contrib import admin
from .models import AnalysisInput, AnalysisResult

# Register your models here.
admin.site.register(AnalysisInput)
admin.site.register(AnalysisResult)