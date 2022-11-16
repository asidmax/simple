from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('simplestart/', include('simplestart.urls')),
    path('admin/', admin.site.urls),
]
