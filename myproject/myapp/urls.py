from django.urls import path
from .views import all_users, all_users_view, delete_user, home_view, login_view, register, login, registration_view, update_user_details, user_details, user_details_view  # Importing views directly
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name='login'),  # Path for the login page
    path('register/', registration_view, name='register'),  # Path for the registration page
    path('home/', home_view, name='home'),  # Home page view
    path('api/login/', login, name='api-login'),  # API endpoint for login
    path('logout/', LogoutView.as_view(), name='logout'),  # Using Django's built-in LogoutView
    path('api/register/', register, name='api-register'),  # API endpoint for registration
    path('api/user-details/', user_details, name='api-user-details'),  # API endpoint for user details
    path('user-details/', user_details_view, name='user-details'),
    path('api/update-user-details/', update_user_details, name='update-user-details'),
    path('api/all-users/', all_users, name='all-users'),
    path('api/delete-user/<str:username>/', delete_user, name='delete-user'),
    path('all-users/', all_users_view, name='all-users-view'),
]