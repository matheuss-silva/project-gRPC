import { NotificationServicePromiseClient } from './notifications_grpc_web_pb.js';
import { NotificationRequest } from './notifications_pb.js';

const client = new NotificationServicePromiseClient('http://localhost:8080', null, null);

const request = new NotificationRequest();
request.setMessage("Hello from the client!");

client.sendNotification(request, {}).then(response => {
    console.log("Resposta recebida:", response.getMessage());
}).catch(err => {
    console.error("Erro ao enviar notificação:", err);
});

const stream = client.subscribeToNotifications(request);
stream.on('data', function(response) {
  console.log('Received notification:', response.getMessage());
});

