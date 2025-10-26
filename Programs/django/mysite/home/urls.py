from django.urls import path
from . import views

urlpatterns = [
    path('bb', views.homeCall),
    path('a',views.addform),
    path('add',views.addVal)
]
       