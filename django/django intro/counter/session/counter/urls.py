from . import views
from django.urls import path

urlpatterns=[
    path('',views.index),
    path('destroy_session',views.dele)
]