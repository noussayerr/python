from django.urls import path, include           

urlpatterns = [
    path('', include('main.urls')),
    path('time_display/', include('main.urls'))  
]