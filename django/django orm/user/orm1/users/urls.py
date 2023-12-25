from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add_user',views.add),
    path('user_add',views.user_to_add)
]