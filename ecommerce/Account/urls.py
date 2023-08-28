from django.urls import path
from .views import UserRegistrationView,UserLoginView,userProfileView,UserChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView,UserLogoutView


urlpatterns = [
  path("register/",UserRegistrationView.as_view(),name="register"),
  path("login/",UserLoginView.as_view(),name="login"),
  path("logout/",UserLogoutView.as_view(),name="logout"),
  path("profile/",userProfileView.as_view(),name="profile"),
  path("changepassword/",UserChangePasswordView.as_view(),name="changepassword"),
  path("send-reset-password-email/",SendPasswordResetEmailView.as_view(),name="send-reset-password-email"),
  path("reset-password/<uid>/<token>/",UserPasswordResetView.as_view(),name="reset-password"),
]
