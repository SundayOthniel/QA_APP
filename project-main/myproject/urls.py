"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from app.views import courses
# from app.views import home
# from app.views import login
# from app.views import profile
# from app.views import questions
# from app.views import register
# from app.views import student
# from app.views import teachers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    # path('student/', student, name='student'),
    # path('teachers/', teachers, name='teachers'),
    # path('questions/', questions, name='questions'),
    # path('courses/', courses, name='courses'),
    # path('', home, name='home'),
    # path('profile/', profile, name='profile'),
    # path('login/', login, name='login'),
    # path('auth/', include("django.contrib.auth.urls"), name="auth"),
    # path('auth/register/', register, name="register")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
