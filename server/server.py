import os
import django
from concurrent import futures
import grpc

import os
import django

# Configurar o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification_admin.notification_admin.settings')
django.setup()

# Importações devem vir após django.setup()
from notification_admin.notifications.models import Notification
from generated import notifications_pb2_grpc, notifications_pb2

class NotificationsServicer(notifications_pb2_grpc.NotificationsServicer):
    def SendNotification(self, request, context):
        notification = Notification(
            recipient_id=request.recipient_id,
            title=request.title,
            message=request.message,
            read=False,
            sent=True,
            created_at=request.created_at.ToDatetime()
        )
        notification.save()
        return notifications_pb2.MarkAsReadResponse(success=True)

    def ListNotifications(self, request, context):
        notifications = Notification.objects.filter(recipient_id=request.user_id)
        response = notifications_pb2.ListNotificationsResponse()
        for notification in notifications:
            n = response.notifications.add()
            n.id = notification.id
            n.recipient_id = notification.recipient_id
            n.title = notification.title
            n.message = notification.message
            n.read = notification.read
            n.sent = notification.sent
            n.created_at.FromDatetime(notification.created_at)
        return response

    def MarkNotificationAsRead(self, request, context):
        try:
            notification = Notification.objects.get(id=request.notification_id)
            notification.read = True
            notification.save()
            return notifications_pb2.MarkAsReadResponse(success=True)
        except Notification.DoesNotExist:
            return notifications_pb2.MarkAsReadResponse(success=False)

    def SubscribeToNotifications(self, request, context):
        pass  # Este método deve ser implementado conforme a lógica da sua aplicação

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notifications_pb2_grpc.add_NotificationsServicer_to_server(NotificationsServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC iniciado na porta 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
