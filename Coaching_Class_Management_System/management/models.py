
from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    # Additional field(s) like 'role' can be added to the user model
    role = models.CharField(max_length=10, choices=[
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    ])
    
    # You can add any other fields as required for your user
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username  # You can also return any other relevant field



class MentorshipSession(models.Model):
    # Student details
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Optional phone number
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    
    # Session details
    session_type_choices = [
        ('career', 'Career Guidance'),
        ('academic', 'Academic Help'),
        ('wellness', 'Mental Wellness'),
    ]
    session_type = models.CharField(max_length=20, choices=session_type_choices)
    
    description = models.TextField()
    
    mode_choices = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]
    mode_of_session = models.CharField(max_length=10, choices=mode_choices)
    
    additional_notes = models.TextField(blank=True, null=True)  # Optional additional notes
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # ... existing fields ...

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    
    def __str__(self):
        return f"{self.full_name} - {self.session_type} on {self.preferred_date} at {self.preferred_time}"


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    details = models.TextField()
    duration = models.CharField(max_length=100)
    fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Content(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    course_tag = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    uploaded_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title


