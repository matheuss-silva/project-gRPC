"use strict";

// Importando as classes necessárias do stub gerado
import { NotificationServicePromiseClient } from './notifications_grpc_web_pb.js';
import { NotificationRequest } from './notifications_pb.js';

// Criar uma nova instância do cliente que aponta para o proxy Envoy
const client = new NotificationServicePromiseClient('http://localhost:8080', null, null);

// Criar uma nova instância de requisição
const request = new NotificationRequest();
request.setMessage("Hello from the client!");

// Enviar uma notificação usando o cliente
client.sendNotification(request, {}).then(response => {
    console.log("Resposta recebida:", response.getMessage());
}).catch(err => {
    console.error("Erro ao enviar notificação:", err);
});

// Assinar notificações
const stream = client.subscribeToNotifications(request);
stream.on('data', function(response) {
    console.log('Received notification:', response.getMessage());
});

