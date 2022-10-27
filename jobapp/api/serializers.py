from rest_framework import serializers
from jobapp.models import JobAdvert, JobApplication


class JobAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAdvert
        fields = ['title', 'company_name', 'employment_type', 'experience_level', 'description', 'location', 'job_description']



class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['first_name', 'last_name', 'email_address', 'phone', 'linkedin_profile_url', 'github_profile_url', 'website', 'years_of_experience', 'cover_letter']