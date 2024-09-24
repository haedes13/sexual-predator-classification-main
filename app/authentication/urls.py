from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path 
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='authentication/login.html', next_page='post-list'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
