from django.contrib import admin
from .models import Notification
from .views import send_notification 

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'message')
    actions = ['send_notifications']

    def send_notifications(self, request, queryset):
        for notification in queryset:
            send_notification(notification.id)
        self.message_user(request, "Notificações enviadas com sucesso!")

admin.site.register(Notification, NotificationAdmin)

