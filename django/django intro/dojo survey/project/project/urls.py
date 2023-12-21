
from django.urls import path,include

urlpatterns = [
    path('', include('post_app.urls')),
]
