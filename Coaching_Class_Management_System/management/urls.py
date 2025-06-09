from django.urls import path
from . import views
from .views import confirm_mentorship_session

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('', views.base, name='base'),
    path('logout/', views.user_logout, name='logout'),
    path('teacher-dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('register/', views.register_user, name='register'),
    path('courses_update/', views.courses_update, name='courses_update'),
    path('materials_list/', views.materials_list, name='materials_list'),
    path('materials_upload/', views.materials_upload, name='materials_upload'),
    path('edit/<int:pk>/', views.materials_upload, name='materials_edit'),
    path('delete/<int:pk>/', views.materials_delete, name='materials_delete'),
    path('book_session/', views.book_session, name='book_session'),
    path('session_list/', views.session_list, name='session_list'),
    path('delete_session/<int:session_id>/', views.delete_session, name='delete_session'),
    path('student_book_session/', views.student_book_session, name='student_book_session'),
    path('courses_list/', views.courses_list, name='courses_list'),
    path('delete-course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('edit-course/<int:course_id>/', views.edit_course, name='edit_course'),
    path('payment', views.payment, name='payment'),
    path('confirm-session/<int:session_id>/', confirm_mentorship_session, name='confirm_session'),
    path('subscribe/', views.subscribe, name='subscribe'),   
    path('send-message/', views.send_mail_view, name='send_mail_view')




]
