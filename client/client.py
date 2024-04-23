import grpc
from generated import notifications_pb2_grpc, notifications_pb2

def run():
    # Inicia uma conexão gRPC com o servidor
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = notifications_pb2_grpc.NotificationsStub(channel)
        # Cria a requisição
        request = notifications_pb2.NotificationRequest(user_id='1', message='notificação enviada')
        # Faz a chamada RPC
        response = stub.SendNotification(request)
        print(f"Cliente recebeu: {response.response_message}")

if __name__ == '__main__':
    run()