
from django.urls import path
from .import views

urlpatterns = [
    path('performance/',views.home,name='home' ),
    path('add/',views.add_purchase,name='add_purchase'),
    path('sales/',views.sales_dist_view,name='sales_dist'),
    path('',views.fund,name='fund'),

]