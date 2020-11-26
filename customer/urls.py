from django.urls import path
from .import views

urlpatterns = [
    path('correlation/',views.customer_corr_view,name='customer_corr'),


]