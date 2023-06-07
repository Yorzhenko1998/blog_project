"""Defines URL patterns for learning_logs."""

from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
	# Add URL auth (authentication).
	path('', include('django.contrib.auth.urls')),
	# Registration page.
	path('register/', views.register, name='register'),
]