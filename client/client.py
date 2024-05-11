import grpc
from generated import notifications_pb2, notifications_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = notifications_pb2_grpc.NotificationsStub(channel)
        # Lista todas as notificações
        list_request = notifications_pb2.ListNotificationsRequest(user_id='1')
        list_response = stub.ListNotifications(list_request)
        print("Notificações recebidas:", list_response.notifications)

        # Marca uma notificação como lida
        mark_request = notifications_pb2.MarkAsReadRequest(notification_id='123')
        mark_response = stub.MarkNotificationAsRead(mark_request)
        print("Marcação como lida:", mark_response.success)

if __name__ == '__main__':
    run()
