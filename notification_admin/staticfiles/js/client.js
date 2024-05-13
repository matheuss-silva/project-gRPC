const {NotificationServicePromiseClient} = require('./generated/notifications_pb_service'); "verificar esses notifications_pb_service"
const {NotificationRequest} = require('./generated/notifications_pb');

var client = new NotificationServicePromiseClient('http://localhost:8080', null, null);

var request = new NotificationRequest();
request.setMessage("Hello from the client!");

client.sendNotification(request, {}, (err, response) => {
  if (err) {
      console.error("Erro ao enviar notificação:", err);
  } else {
      console.log("Resposta recebida:", response.getMessage());
  }
});

const stream = client.subscribeToNotifications(request);
stream.on('data', function(response) {
  console.log('Received notification:', response.getMessage());
});
