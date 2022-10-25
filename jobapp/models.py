from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


EMOPLOYMENT_TYPE = (
    ('FULL_TIME', 'Full-time'),
    ('CONTRACT', 'Contract'),
    ('REMOTE', 'Remote'),
    ('PART_TIME', 'Part-time'),
)
EXPERIENCE_LEVEL = (
    ('ENTRY_LEVEL', 'Entry-level'),
    ('MID_LEVEL', 'Mid-level'),
    ('SENIOR', 'Senior'),
)
class JobAdvert(models.Model): 
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    title = models.CharField(max_length=150, blank=False)
    company_name = models.CharField(max_length=150, blank=False)
    employment_type = models.CharField(choices=EMOPLOYMENT_TYPE, max_length=30, blank=True)
    experience_level = models.CharField(choices=EXPERIENCE_LEVEL, max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=False)
    location = models.CharField(max_length=150, null=True, blank=False)
    job_description = models.TextField(null=True, blank=False) ## NOTE ask teacher
    published = models.BooleanField(default=True, null=True, blank=False)
    
    def __str__(self) -> str:
        return f'{self.title} by {self.owner}'


# - First name
# - Last name
# - Email address
# - Phone
# - Linkedin profile URL
# - GitHub profile URL
# - Website (optional)
# - Years of experience (0 - 1, 1 - 2, 3 - 4, 5 - 6, 7 and above)
# - Cover letter (Should be optional and can be a CharField)
YEARS_OF_EXPERIENCE = (
    ('1_', '0 - 1'),
    ('2_', '1 - 2'),
    ('3_', '3 - 4'),
    ('4_', '5 - 6'),
    ('5_', '7 and above'),
)
class JobApplication(models.Model):
    applicants = models.ForeignKey(JobAdvert, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email_address = models.EmailField()
    phone = models.BigIntegerField()
    linkedin_profile_url = models.URLField()
    github_profile_url = models.URLField()
    website = models.URLField()
    years_of_experience = models.CharField(max_length=30, choices=YEARS_OF_EXPERIENCE)