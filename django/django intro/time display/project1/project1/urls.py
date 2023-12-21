from django.urls import path, include           

urlpatterns = [
    path('', include('time_display.urls')),
    path('time_display/', include('time_display.urls'))  
]