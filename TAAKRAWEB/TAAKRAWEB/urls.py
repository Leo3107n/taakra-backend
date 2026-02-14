"""
URL configuration for TAAKRAWEB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from core import views
from core.views import (
    RegisterView,
    CategoryListView,
    CompetitionListView,
    CompetitionDetailView,
    RegisterCompetitionView,
    MyRegistrationsView,
    MostRegisteredCompetitionsView,
    NewCompetitionsView,
    TrendingCompetitionsView,
    AIChatBotView
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', views.RegisterView.as_view(), name='register'),

    path('api/categories/', CategoryListView.as_view(), name='categories'),
    path('api/competitions/', CompetitionListView.as_view(), name='competitions'),
    path('api/competitions/<int:pk>/', CompetitionDetailView.as_view(), name='competition-detail'),
    path('api/register-competition/', RegisterCompetitionView.as_view(), name='register-competition'),
    path('api/my-registrations/', MyRegistrationsView.as_view(), name='my-registrations'),
    path('api/competitions/most-registered/', MostRegisteredCompetitionsView.as_view(), name='competitions-most-registered'),
    path('api/competitions/new/', NewCompetitionsView.as_view(), name='competitions-new'),
    path('api/competitions/trending/', TrendingCompetitionsView.as_view(), name='competitions-trending'),
    path('api/ai-chat/', AIChatBotView.as_view(), name='ai-chat'),


]
