from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser
from .models import MentorshipSession
from .models import Course
from .models import Content

class CustomUserForm(UserCreationForm):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'password1', 'password2')



class MentorshipSessionForm(forms.ModelForm):
    class Meta:
        model = MentorshipSession
        fields = '__all__'
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'preferred_time': forms.TimeInput(attrs={'type': 'time'}),
        }



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'details', 'duration', 'fees']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'rows': 3}),
            'duration': forms.TextInput(),
            'fees': forms.NumberInput(),
        }



class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'description', 'course_tag', 'price', 'uploaded_file']


