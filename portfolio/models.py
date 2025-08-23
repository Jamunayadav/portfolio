from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    website = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    about_me = models.TextField()
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Personal Info"

    def __str__(self):
        return self.name

class Skill(models.Model):
    SKILL_CATEGORIES = [
        ('programming', 'Programming Languages'),
        ('database', 'Databases'),
        ('cloud', 'Cloud Platforms'),
        ('tools', 'Tools & Technologies'),
        ('soft', 'Soft Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)
    proficiency = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Skill proficiency level (1-100)"
    )
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome icon class")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.ManyToManyField(Skill, related_name='projects')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-featured', 'order', '-created_at']
    
    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField()
    achievements = models.TextField(blank=True)
    technologies_used = models.ManyToManyField(Skill, related_name='experiences', blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date', 'order']
    
    def __str__(self):
        return f"{self.position} at {self.company}"

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date', 'order']
    
    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution}"

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiry_date = models.DateField(blank=True, null=True)
    credential_id = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='certifications/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-issue_date', 'order']
    
    def __str__(self):
        return f"{self.name} from {self.issuing_organization}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    excerpt = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
