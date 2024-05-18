import os
import django
from concurrent import futures
import grpc

# Configurar o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notification_admin.notification_admin.settings')


django.setup()

# Importar os módulos necessários após configurar o ambiente do Django
from notifications import Notification
from generated import notifications_pb2_grpc, notifications_pb2

class NotificationsServicer(notifications_pb2_grpc.NotificationsServicer):
    def SendNotification(self, request, context):
        # Implementação do método SendNotification
        notification = Notification(
            recipient_id=request.recipient_id,
            title=request.title,
            message=request.message,
            read=request.read,
            sent=request.sent,
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
        # Este método deve ser implementado conforme a lógica da sua aplicação
        pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notifications_pb2_grpc.add_NotificationsServicer_to_server(NotificationsServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC iniciado na porta 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()


'''from concurrent import futures
import grpc
from generated import notifications_pb2_grpc, notifications_pb2
import sys
sys.path.append('D:/Documentos/Projetos/project-gRPC/notification_admin')
from notifications.models import Notification

def fetch_notifications():
    # Busca todas as notificações que ainda não foram enviadas
    return Notification.objects.filter(sent=False)

def process_notification(user_id, message):
    # Aqui você implementaria a lógica para processar a notificação
    # Por exemplo, salvar no banco de dados ou enviar através de um serviço externo
    print(f"Processando notificação para o usuário {user_id} com a mensagem: '{message}'")
    # Simulação de um processo que pode falhar
    if not user_id or not message:
        raise ValueError("UserID ou mensagem não fornecidos")
    # Simule um processo bem-sucedido
    print("Notificação processada com sucesso")

class NotificationsServicer(notifications_pb2_grpc.NotificationsServicer):
    def SendNotification(self, request, context):
        try:
            print(f"Enviando notificação para o usuário {request.user_id} com a mensagem: {request.message}")
            # Chama a função que realmente processa a notificação
            process_notification(request.user_id, request.message)
            return notifications_pb2.NotificationResponse(success=True, response_message="Notificação enviada com sucesso.")
        except Exception as e:
            print(f"Erro ao enviar notificação: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('Failed to send notification')
            return notifications_pb2.NotificationResponse(success=False, response_message="Erro ao enviar notificação")

    
    def SubscribeToNotifications(self, request, context):
        # verificaria novas notificações em seu banco de dados
        # Para demonstração, enviamos apenas algumas notificações fictícias
        yield notifications_pb2.NotificationResponse(title="Welcome", message="Hello, this is your notification service", isRead=False)
        
    def ListNotifications(self, request, context):
        try:
            notifications = fetch_notifications()
            response = notifications_pb2.ListNotificationsResponse()
            for notification in notifications:
                # Cria um novo objeto Notification e preenche os campos
                proto_notification = response.notifications.add()
                proto_notification.id = str(notification.id)  # Garanta que o ID seja uma string
                proto_notification.title = notification.title
                proto_notification.message = notification.message
                proto_notification.read = notification.read
            return response
        except Exception as e:
            print("Erro ao serializar a resposta:", e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details('Failed to serialize response!')
            return None

    def MarkNotificationAsRead(self, request, context):
        # Implemente a lógica para marcar uma notificação como lida
        pass

# Iniciar o servidor
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notifications_pb2_grpc.add_NotificationsServicer_to_server(NotificationsServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor iniciado na porta 50051.")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
'''