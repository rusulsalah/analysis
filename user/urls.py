from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_view,name='login'),
    path('logout/', views.logout_func, name='logout'),
    path('signup/', views.signup_form, name='signup'),
    ]