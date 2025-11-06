"""
URL configuration for onlinecompiler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication (custom user management)
    path('api/auth/', include('authentication.urls')),
    
    # # OAuth (Google login etc. through allauth)
    # path('accounts/', include('allauth.urls')),

    # # Problems (CRUD and problem listing)
    # path('api/problems/', include('problems.urls')),

    # # Test Cases (linked to problems)
    # path('api/testcases/', include('testcases.urls')),

    # # Code Compiler / Execution
    # path('api/compiler/', include('compiler.urls')),

    # # Submissions (user code submissions, verdicts, history)
    # path('api/submissions/', include('submissions.urls')),

    # # Dashboard (user performance and stats)
    # path('api/dashboard/', include('dashboard.urls')),

    # # Leaderboard
    # path('api/leaderboard/', include('leaderboard.urls')),

]

# Serve media & static files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
