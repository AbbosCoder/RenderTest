from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField()
    linkedin = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    x = models.URLField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.full_name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=255, help_text="Texnologiyalarni vergul bilan ajrating.")
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def get_technologies_list(self):
        return self.technologies.split(',')

    def __str__(self):
        return self.title

class Skill(models.Model):
    LEVEL_CHOICES = [
        ("Junior", "Junior"),
        ("Middle", "Middle"),
        ("Senior", "Senior"),
        ("Lead", "Lead"),
        ("Expert", "Expert"),
    ]

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)

class MyInfo(models.Model):
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"
