from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('/analysis', views.index, name='predict'),
    path('/plans',views.plans,name='plans'),
]
