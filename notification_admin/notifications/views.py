import grpc
from generated import notifications_pb2, notifications_pb2_grpc
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Notification

def send_notification(notification_id):
    notification = Notification.objects.get(id=notification_id)
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = notifications_pb2_grpc.NotificationsStub(channel)
        request = notifications_pb2.NotificationRequest(
            user_id='1',
            message=notification.message
        )
        response = stub.SendNotification(request)
        if response.success:
            notification.sent = True
            notification.save()
            print("Notificação enviada com sucesso!")
        else:
            print("Falha ao enviar a notificação.")

@login_required
def user_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-created_at')
    return render(request, 'notifications/user_notifications.html', {'notifications': notifications})
