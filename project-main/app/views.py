from django.contrib.auth import authenticate, login
from .models import Users
# from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
# from django.urls import reverse
# from .models import Student, Teacher, Question, Course, Answer
from django.contrib import messages



# View for listing all students

def register(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    uname = request.POST.get("uname")
    user = request.POST.get("student-teacher")
    password = request.POST.get("password")
    c_pass = request.POST.get("c_pass")
    
    name_exist = Users.user_manager.username(name)
    emil_exist = Users.user_manager.username(email)
    
    if request.method == "POST":
        if name_exist:
            messages.error(request, f"This user \"{name}\" already exist")
            return redirect('app:user-registration')
        elif password != c_pass:
            # if len(password) < 1:
            #     messages.error(request, f"The length of your password is too short")
            messages.error(request, f"Password does not match")
            return redirect('app:user-registration')
        elif emil_exist:
            messages.error(request, f"This provided \"{email}\" already exist")
            return redirect('app:user-registration')
        elif password == c_pass:
            if user == 'student':
                user = Users.user_manager.create(username=uname, name=name, email=email, user=user)
                user.set_password(password)
                user.save()
                return redirect('app:user-registration')
            else:
                user = Users.user_manager.create(username=uname, name=name, email=email, user=user)
                user.set_password(password)
                user.save()
                return redirect('app:user-registration')
    return render(request, 'registration/register.html')

        



# def student(request):
#     student = Student.objects.all()
#     return render(request, 'student.html/', {'student': student})


# # View for creating a new student
# def student_create(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         department = request.POST.get('department')
#         contact_information = request.POST.get('contact_information')
#         preferences = request.POST.get('preferences')
#         student = Student.objects.create(name=name, department=department, contact_information=contact_information,
#                                          preferences=preferences)
#         return redirect(reverse('student'))
#     return render(request, 'student_create.html')


# # View for listing all teachers
# def teachers(request):
#     teachers = Teacher.objects.all()
#     return render(request, 'teachers.html/', {'teachers': teachers})


# # View for creating a new teacher
# def teacher_create(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         subject_specifization = request.POST.get('subject_specifization')
#         contact_information = request.POST.get('contact_information')
#         teacher = Teacher.objects.create(name=name, subject_specifization=subject_specifization,
#                                          contact_information=contact_information)
#         return redirect(reverse('teacher'))
#     return render(request, 'teacher_create.html')


# # View for listing all questions
# def questions(request):
#     questions = Question.objects.all()
#     return render(request, 'questions.html/', {'questions': questions})


# # View for creating a new question
# def question_create(request):
#     if request.method == 'POST':
#         student_id = request.POST.get('student_id')
#         content = request.POST.get('content')
#         student = Student.objects.get(id=student_id)
#         question = Question.objects.create(student=student, content=content)
#         return redirect(reverse('questions'))
#     students = Student.objects.all()
#     return render(request, 'question_create.html', {'students': students})


# def courses(request):
#     courses = Course.objects.all()
#     context = {'courses': courses}
#     return render(request, 'courses.html/', context)


# def home(request):
#     if request.Users.is_authenticated:
#         return render(request, 'home.html')
#     else:
#         return redirect(reverse('login'))


# def profile(request):
#     return render(request, 'profile.html/')


# def answers(request):
#     answers = Answer.objects.all()
#     context = {'answers': answers}
#     return render(request, 'answers.html', context)

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('password')
        authenticate_user = authenticate(username=username, password=password)
        if authenticate_user is not None:
            user = Users.user_manager.get().first()
            if user.user == 'teacher':
                login(request, authenticate_user) 
                return redirect('teacher:teacher_dashboard')
            else:
                login(request, authenticate_user) 
                return redirect('student:student_dashboard')
        else:
            messages.error(request, "Reconfirm your login details")
            return redirect('app:user-login')
    return render(request, 'registration/login.html')


# def save(self, commit = True):
#             Users = super('RegisterForm', self).save(commit = False)
#             Users.username = self.cleaned_data.get("username", None)
#             Users.first_name = self.cleaned_data.get("first_name", None)
#             Users.last_name = self.cleaned_data.get("last_name", None)
#             Users.email = self.cleaned_data.get("email", None)

#             if commit:

#                 Users.save()

#             return Users