# 🏥 Care & Cure - Hospital Management System

A responsive, web-based Hospital Management System built using Django to streamline daily hospital operations, manage medical staff, and provide seamless online booking services for patients.

🚀 **Live Website Link:** https://care-and-cure-hospital.onrender.com/

---

## ✨ Key Features

* **🚨 Emergency Fixed Alert:** A prominent emergency card with a smooth pulse animation for instant emergency dialing.
* **📅 Appointment Booking:** Patients can choose their preferred doctors and book appointments online.
* **🕒 Live Working Hours Alert:** Dynamic live status indicators displaying whether the hospital/department is currently "Open" or "Closed".
* **🩺 Interactive Department Filter:** Seamlessly filter and view available doctors based on specialized departments (e.g., Cardiology, Pediatrics, Neurology).
* **🔐 Django Admin Panel:** A secure, built-in administrative dashboard for hospital staff to effortlessly manage doctors, patient records, and appointments.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Render](https://img.shields.io/badge/Render-%2346E3B7.svg?style=for-the-badge&logo=render&logoColor=white)

* **Backend:** Django (Python 3.x)
* **Frontend:** HTML5, CSS3, Bootstrap 5 (Fully Responsive)
* **Database:** SQLite (Default Django DB)
* **Static File Management:** Whitenoise
* **Hosting:** Render

---

## 💻 How to Run This Project on Your Local Machine

Follow these step-by-step instructions to get a development envrionment running locally.

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/care-cure-hospital.git](https://github.com/your-username/care-cure-hospital.git)
cd web
```
### 2. Set Up a Virtual Environment (Recommended):
```bash
# Create a virtual environment
python -m venv venv
# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run Database Migrations
```bash
python manage.py migrate
### 5. Create an Admin Account (For the Admin Panel)
#create a superuser account:
python manage.py createsuperuser
#type a username
#type a emil
#type a password
#To log into the /admin dashboard and add doctors or departments,
```
### 3. Run the development server:
```bash
python manage.py runserver
```
