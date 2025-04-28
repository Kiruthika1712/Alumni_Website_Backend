"""
URL configuration for footrpints project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from core import views
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/verifyUser/', views.alumni_list),
    path('api/emailv/',v.email_verification),
    path('api/otpv/<str:email>/',v.verify_otp),
    path('api/resend/', v.resend_otp),
    path('api/event-categories', views.event_categories_list),
    path('api/event-categories/<int:id>', views.events_list),
    path('api/events', views.events_list_home),
    path('api/news-categories', views.news_categories_list),
    path('api/news-categories/<int:id>', views.news_list),
    path('api/news', views.news_list_home),
    path('api/blogs', views.blogs),
    path('api/mentors', views.mentor),
    path('api/mentees/<int:id>', views.mentee),
    path('api/gallery', views.gallery),
    path('api/non-monetary-contribution/', views.non_monetary_contribution, name='non-monetary-contribution'),
    path('api/lor/', views.letter_of_recommendation, name='letter_of_recommendation'),
    path('api/class-note/', views.class_note, name='class_note'),
]

