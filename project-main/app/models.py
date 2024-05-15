# from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models


# Create your models here.
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     department = models.CharField(max_length=100,  blank=True)
#     contact_information = models.CharField(max_length=255, blank=True)
#     user= models.ForeignKey(User, on_delete=models.CASCADE)

#     def _str_(self):
#         return self.name


# class Teacher(models.Model):
#     name = models.CharField(max_length=255)
#     subject_specifization = models.CharField(max_length=255,  blank=True)
#     contact_information = models.CharField(max_length=255, blank=True)
#     user= models.ForeignKey(User, on_delete= models.CASCADE)

#     def _str_(self):
#         return self.name


# class Question(models.Model):
#     student = models.ForeignKey(Student,
#                                 on_delete=models.CASCADE)  # ForeignKey establishes a many-to-one relationship with Student
#     timestamp = models.DateTimeField(auto_now_add=True)
#     content = models.TextField()
#     status = models.CharField(max_length=20, default='open')

#     def _str_(self):
#         return f"Question {self.id} by {self.student.name}"


# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE,
#                                  related_name='answers')  # ForeignKey establishes a many-to-one relationship with Question
#     teacher = models.ForeignKey(Teacher,
#                                 on_delete=models.CASCADE)  # ForeignKey establishes a many-to-one relationship with Teacher
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Answer {self.id} to Question {self.question.id} by {self.teacher.name}"


# class Course(models.Model):
#     title = models.CharField(max_length=255)
#     tutor = models.CharField(max_length=100)
#     date_added = models.DateField(auto_now_add=True)
#     description = models.TextField()
#     thumbnail = models.ImageField(upload_to='image/')

#     def __str__(self):
#         return self.title


class UserManager(models.Manager):
    """
    Custom manager class for querying the User model.

    Example Usage:
    user_manager = UserManager()
    user_exists = user_manager.username('John')
    email_exists = user_manager.email('john@example.com')     

    Methods:
    - username(name): Returns a boolean indicating whether a user with the given name exists.
    - email(email): Returns a boolean indicating whether a user with the given email exists.
    """

    def username(self, name):
        """
        Check if a user with the given name exists.

        Args:
        - name (str): The name to check.

        Returns:
        - bool: True if a user with the given name exists, False otherwise.
        """
        return super().get_queryset().filter(name=name).exists()

    def email(self, email):
        """
        Check if a user with the given email exists.

        Args:
        - email (str): The email to check.

        Returns:
        - bool: True if a user with the given email exists, False otherwise.
        """
        return super().get_queryset().filter(email=email).exists()
    
    def get_by_natural_key(self, username):
        return self.get(username=username)
class Users(AbstractUser):
    """
    Represents a user in the system with various user-related fields.

    Fields:
    - name: A character field representing the user's name.
    - user: A character field representing the user.
    - student_teacher: A character field representing the user's role as a student or teacher.
    - first_name: A character field representing the user's first name.
    - username: A character field representing the user's username.
    - last_name: A character field representing the user's last name.

    Methods:
    - __str__(): Returns a string representation of the user's name.
    - username(name): Checks if a user with the given name exists.
    - email(email): Checks if a user with the given email exists.
    """

    name = models.CharField(max_length=150, blank=False, null=False, default='')
    user = models.CharField(max_length=255, null=False, blank=False, default='')
    
   
    class Meta:
        db_table = 'user_authentication'

    user_manager = UserManager()

    def __str__(self):
        """
        Returns a string representation of the user's name.
        """
        return self.name


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=65)
#     password = forms.CharField(max_length=65, widget=forms.PasswordInput)


# class RegisterForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
