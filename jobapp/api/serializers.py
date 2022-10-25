from rest_framework import serializers
from jobapp.models import JobAdvert


class JobAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAdvert
        fields = ['title', 'company_name', 'employment_type', 'experience_level', 'description', 'location', 'job_description']