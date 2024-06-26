from . import views
from django.urls import path
from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', views.UserRegistration.as_view(), name='registration'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('edit/<slug:slug>/', views.UpdatePost.as_view(), name='edit'),
    path('delete/<slug:slug>/', views.DeletePost.as_view(), name='delete'),
    path('profile/', views.UserProfile.as_view(), name='profile'),
    path('password_change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('back_to_profile/done/', views.UserPasswordChangeDone.as_view(), name='back_to_profile'),
    path('password_reset/', views.UserPasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', views.UserPasswordResetDone.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', views.UserPasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', views.UserPasswordResetComplete.as_view(), name='password_reset_complete'),
]
