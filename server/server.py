from concurrent import futures
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