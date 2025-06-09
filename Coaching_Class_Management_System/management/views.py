from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserForm
from .models import CustomUser
from django.contrib import messages
from .forms import MentorshipSessionForm
from .models import MentorshipSession
from .models import Course
from .models import Content
from .forms import ContentForm
from django.core.mail import send_mail
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')
        send_mail(
            subject="Welcome to MentorDesk – Unleash Your Learning Potential!",
            message="""Dear Student,

We’re thrilled to welcome you to MentorDesk, a platform designed to empower your learning journey with expert guidance, interactive courses, and personalized mentorship!

What Awaits You at MentorDesk?
🎓 Expert Mentors – Learn from top educators who care about your success.
📖 Custom Course Content – Access materials tailored to your unique learning style.
💡 Stress-Free Mentorship – Academic guidance that also supports your well-being.
🤝 Peer Collaborations – Engage in group sessions and exciting projects.

If you have any questions or need assistance, feel free to reach out to our support team.

Best regards,
The MentorDesk Team
""",
            from_email="your_email@example.com",  # replace with your email
            recipient_list=[email],
            fail_silently=False,
        )
        messages.success(request, "Subscription successful! Check your email.")
        return redirect('base')  # or your homepage URL name


def user_login(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"Received login attempt - Username: {username}")  # DEBUG

        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(f"Authenticated user: {user.username}, Role: {user.role}")  # DEBUG
            login(request, user)

            if user.role == 'teacher':  # ✅ Teacher is your admin
                print("Redirecting to admin dashboard")
                return redirect('teacher_dashboard')

            elif user.role == 'student':
                print("Redirecting to student dashboard")
                return redirect('student_dashboard')

            else:
                print("No matching role found")
                messages.error(request, "Unknown role. Contact admin.")
                return redirect('login')

        else:
            print("Authentication failed")
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, 'login.html')  # ✅ Don't include leading slash



@login_required
def user_logout(request):
    logout(request)
    return redirect('base')

@login_required
def teacher_dashboard(request):
    total_courses = Course.objects.count()
    total_materials = Content.objects.count()
    total_students = CustomUser.objects.filter(role='student').count()
    
    context = {
        'total_courses': total_courses,
        'total_materials': total_materials,
        'total_students': total_students,
    }
    
    return render(request, 'dashboard/teacher_dashboard.html', context)

@login_required
def student_dashboard(request):
    
    return render(request, 'dashboard/student_dashboard.html')

def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("registration successfull")
            return redirect('login')
              # after successful registration
    else:
        form = CustomUserForm()
    return render(request, 'register.html', {'form': form})


def base(request):
    return render(request, 'base.html')


def book_session(request): 
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        preferred_date = request.POST.get('date')
        preferred_time = request.POST.get('time')
        session_type = request.POST.get('type')
        description = request.POST.get('concern')
        mode_of_session = request.POST.get('mode')
        phone_number = request.POST.get('phone') 
        additional_notes = request.POST.get('notes')  

        a = MentorshipSession.objects.create(
            full_name=full_name,
            email=email,
            preferred_date=preferred_date,
            preferred_time=preferred_time,
            session_type=session_type,
            description=description,
            mode_of_session=mode_of_session,
            phone_number=phone_number,
            additional_notes=additional_notes,
        )
        a.save()
        messages.success(request, "Session booked successfully! Please wait for confirmation.")

    return render(request, 'mentorship/book_session.html')


# Show unconfirmed sessions only
def session_list(request):
    sessions = MentorshipSession.objects.all()
    return render(request, 'mentorship/session_list.html', {'sessions': sessions})


# Delete a session
def delete_session(request, session_id):
    session = get_object_or_404(MentorshipSession, id=session_id)
    session.delete()
    return redirect('session_list')

def student_book_session(request):
    sessions = MentorshipSession.objects.all()
    return render(request, 'mentorship/student_book_session.html', {'sessions': sessions})


def courses_update(request):
    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        name = request.POST.get('name')
        details = request.POST.get('details')
        duration = request.POST.get('duration')
        fees = request.POST.get('fees')


        if course_id:  # Update existing course
            course = get_object_or_404(Course, id=course_id)
            course.name = name
            course.details = details
            course.duration = duration
            course.fees = fees
            course.save()
            messages.success(request, 'Course updated successfully!')
        else:
            # Add new course
            if not Course.objects.filter(name=name).exists():
                x = Course.objects.create(name=name, details=details, duration=duration, fees=fees)
                x.save()
                messages.success(request, 'Course added successfully!')
            else:
                messages.warning(request, 'Course with this name already exists.')

        return redirect('courses_update')
        

    courses = Course.objects.all()
    return render(request, 'courses/courses_update.html', {'courses': courses})


def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    messages.success(request, 'Course deleted successfully!')
    return redirect('courses_update')


def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    courses = Course.objects.all()
    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.details = request.POST.get('details')
        course.duration = request.POST.get('duration')
        course.fees = request.POST.get('fees')
        course.save()
        messages.success(request, 'Course updated successfully!')
        return redirect('courses_update')
    return render(request, 'courses/courses_update.html', {'edit_course': course, 'courses': courses})

def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses_list.html', {'courses': courses})

def payment(request):
    course_id = request.GET.get('course_id')
    course_name = request.GET.get('course_name', 'Selected Course')
    course_fee = request.GET.get('course_fee', '999')
    
    context = {
        'course_name': course_name,
        'course_fee': course_fee,
    }
    
    return render(request, 'payment.html', context)



def send_mail_view(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"""
        You have received a new message from your website contact form.

        Name: {first_name} {last_name}
        Email: {email}
        Phone: {phone}
        Subject: {subject}

        Message:
        {message}
        """

        try:
            send_mail(
                subject=f"New Contact: {subject}",
                message=full_message,
                from_email='webmaster@yourdomain.com',  # Replace with your verified sender email
                recipient_list=['hostemail@example.com'],  # Replace with your host/admin email
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')

        return redirect('base')  # Or wherever your contact page lives

    return redirect('base')
def materials_upload(request, pk=None):
    if pk:
        instance = get_object_or_404(Content, pk=pk)
    else:
        instance = None

    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if pk:
                messages.success(request, "Content successfully updated.")
            else:
                messages.success(request, "Content successfully added.")
            return redirect('materials_upload')
    else:
        form = ContentForm(instance=instance)

    contents = Content.objects.all()
    return render(request, 'materials/materials_upload.html', {
        'form': form,
        'contents': contents,
        'is_edit': pk is not None
    })

def materials_list(request):
    contents = Content.objects.all()
    return render(request, 'materials/materials_list.html', {'contents': contents})

def materials_delete(request, pk):
    content = get_object_or_404(Content, pk=pk)
    if request.method == 'POST':
        content.delete()
        messages.success(request, "Content successfully Deleted.")
        return redirect('materials_upload')
    return render(request, 'confirm_delete.html', {'content': content})

def confirm_mentorship_session(request, session_id):
    session = get_object_or_404(MentorshipSession, id=session_id)
    session.status = 'confirmed'
    session.save()

    subject = "Your Counselling Session is Confirmed"
    message = f"""Dear {session.full_name},

Your Counselling session for "{session.get_session_type_display()}" has been confirmed.

🗓 Date: {session.preferred_date.strftime('%A, %d %B %Y')}
🕒 Time: {session.preferred_time.strftime('%I:%M %p')}
📍 Mode: {session.get_mode_of_session_display()}

Thank you for choosing us!

Regards,
Mentorship Team
"""

    send_mail(
        subject,
        message,
        'your_email@gmail.com',
        [session.email],
        fail_silently=False,
    )

    messages.success(request, "Session confirmed and email sent to the student.")
    return redirect('teacher_dashboard')  # Update this with your actual redirect


