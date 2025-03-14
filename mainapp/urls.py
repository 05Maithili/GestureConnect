#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#urlpatterns += staticfiles_urlpatterns()
# mainapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('signup_signin/', views.signup_signin, name='signup_signin'),
    path('sign_to_text/', views.sign_to_text ,name='sign_to_text'),
    path('sign_to_speech/', views.sign_to_speech, name='sign_to_speech'), 
    path('text_to_speech/', views.text_to_speech, name='text_to_speech'),
    path('speech_to_text/', views.speech_to_text, name='speech_to_text'),
    
]