from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('product-details/<slug>', views.product_details, name='product-details'),
    path('register', views.user_register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('users', views.users, name='users'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='pages/login/password-reset.html'),
         name='password-reset'),
    path('password_reset_confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='pages/login/password-reset-confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_done',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='pages/login/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_complete',
         auth_views.PasswordResetCompleteView.as_view(template_name='pages/login/password_reset_complete.html'),
         name='password_reset_complete')

]
