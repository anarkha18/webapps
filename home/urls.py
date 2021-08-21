from django.urls import path
from home import views

urlpatterns = [
     path('gh', views.gh, name="gh"),
]