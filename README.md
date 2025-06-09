# MentorDesk 🎓📚

MentorDesk is a Django-based web application designed for managing coaching class operations efficiently. It provides separate dashboards and functionalities for **Admins**, **Teachers**, and **Students**, making it ideal for educational institutions and learning centers.

---

## 🚀 Features

- 🧑‍💼 **Admin Panel**: Manage teachers, students, and course content.
- 👩‍🏫 **Teacher Dashboard**: Add courses, upload study materials, manage students.
- 🎓 **Student Portal**: View profile, access course materials.
- 🔐 User authentication (Login/Logout)
- 🗂 Organized views and routing per user role
- 📁 File upload and content management system

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Django
- **Database**: MySQL
- **Tools**: VS Code, MySQL Workbench, Git & GitHub

---

## 🔧 Setup Instructions

Follow these steps to run the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/Pournima87/MentorDesk.git
   cd MentorDesk```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # For Windows
   
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   
4. Configure the database
     - Set up your MySQL database
     - Update settings.py with your DB credentials
       
5. Apply migrations and run server
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   
6. Open in browser
   ```bash
   http://127.0.0.1:8000/

---

## 📂 Folder Structure

MentorDesk/
│
├── Coaching_Class_Management_System/
│   ├── admin/
│   ├── teacher/
│   ├── student/
│   ├── templates/
│   └── ...
├── db.sqlite3
├── manage.py
└── README.md


---




