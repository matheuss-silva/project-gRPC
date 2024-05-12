const {NotificationServicePromiseClient} = require('./generated/notifications_pb_service'); "verificar esses notifications_pb_service"
const {NotificationRequest} = require('./generated/notifications_pb');

const client = new NotificationServicePromiseClient('http://localhost:8080', null, null);

const request = new NotificationRequest();
request.setUserId('1');

const stream = client.subscribeToNotifications(request);
stream.on('data', function(response) {
  console.log('Received notification:', response.getMessage());
});