from django.urls import path
from .import views

urlpatterns = [
    path('test/',views.upload_file_view,name='upload_file_view' ),


]