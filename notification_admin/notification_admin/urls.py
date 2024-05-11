
from django.contrib import admin
from django.urls import path
from notifications.views import user_notifications

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-notifications/', user_notifications, name='user_notifications'),
]
