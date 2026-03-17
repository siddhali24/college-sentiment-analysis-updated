"""
URL configuration for sentiment project.

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
from django.urls import path
from analysis import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('college_info', views.college_info, name='college_info'),
    path('Aboutus', views.Aboutus, name='Aboutus'),
    #path('review', views.review, name='review'),
    path('review', views.sentiment_analysis_view, name='sentiment-review'),
    path('get_college_reviews', views.get_college_reviews, name='get_college_reviews'),
   #path('api/get_college_reviews/', views.get_college_reviews, name='get_college_reviews')

]




