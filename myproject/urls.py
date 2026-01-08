

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('assignments/',include('planner.urls')),
    path('habits/',include('habits.urls')),
    path('',include('dashboard.urls')),
]
