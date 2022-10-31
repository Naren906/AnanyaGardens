from django.urls import path
from AAGardens import views

urlpatterns = [
    path('', views.dash_home, name="dash_home"),
    path('about/', views.about, name="about"),
    path('gallary/', views.gallary, name="gallary"),
    path('projects/', views.projects, name="projects"),
    path('contact/', views.contact, name="contact"),
    path('projectdetails/', views.Projectdetails, name="projectdetails"),
    path('checkotp/', views.checkotp, name="checkotp"),
	path('Projectcompleted1/', views.Projectcompleted1, name="Projectcompleted1"),
]

