from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_frontend(request):
    return redirect('http://localhost:3000/')  # Update with your frontend server URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', redirect_to_frontend),  # Redirect root to frontend
]


