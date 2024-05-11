from concurrent import futures
import grpc
from generated import notifications_pb2_grpc, notifications_pb2


# Métodos do serviço definidos no .proto
class NotificationsServicer(notifications_pb2_grpc.NotificationsServicer):
    def SendNotification(self, request, context):
        print(f"Enviando notificação para o usuário {request.user_id} com a mensagem: {request.message}")
        return notifications_pb2.NotificationResponse(success=True, response_message="Notificação enviada com sucesso.")
        
    def ListNotifications(self, request, context):
        # Implemente a lógica para listar notificações
        pass

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