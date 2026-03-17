from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('college_info', views.college_info, name='college_info'),
    path('Aboutus', views.Aboutus, name='Aboutus'),
    #path('review', views.review, name='review'),
    path('review', views.sentiment_analysis_view, name='sentiment-review'),
    path('get_college_reviews', views.get_college_reviews, name='get_college_reviews'),
   #path('api/get_college_reviews/', views.get_college_reviews, name='get_college_reviews')
    
]


