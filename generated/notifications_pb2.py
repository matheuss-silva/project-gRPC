# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: notifications.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13notifications.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9c\x01\n\x0cNotification\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0crecipient_id\x18\x02 \x01(\x03\x12\r\n\x05title\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x0c\n\x04read\x18\x05 \x01(\x08\x12\x0c\n\x04sent\x18\x06 \x01(\x08\x12.\n\ncreated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"%\n\x13NotificationRequest\x12\x0e\n\x06userId\x18\x01 \x01(\t\"F\n\x14NotificationResponse\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0e\n\x06isRead\x18\x03 \x01(\x08\"+\n\x18ListNotificationsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"A\n\x19ListNotificationsResponse\x12$\n\rnotifications\x18\x01 \x03(\x0b\x32\r.Notification\",\n\x11MarkAsReadRequest\x12\x17\n\x0fnotification_id\x18\x01 \x01(\t\"%\n\x12MarkAsReadResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xa1\x02\n\rNotifications\x12\x36\n\x10SendNotification\x12\r.Notification\x1a\x13.MarkAsReadResponse\x12J\n\x11ListNotifications\x12\x19.ListNotificationsRequest\x1a\x1a.ListNotificationsResponse\x12\x41\n\x16MarkNotificationAsRead\x12\x12.MarkAsReadRequest\x1a\x13.MarkAsReadResponse\x12I\n\x18SubscribeToNotifications\x12\x14.NotificationRequest\x1a\x15.NotificationResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'notifications_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_NOTIFICATION']._serialized_start=57
  _globals['_NOTIFICATION']._serialized_end=213
  _globals['_NOTIFICATIONREQUEST']._serialized_start=215
  _globals['_NOTIFICATIONREQUEST']._serialized_end=252
  _globals['_NOTIFICATIONRESPONSE']._serialized_start=254
  _globals['_NOTIFICATIONRESPONSE']._serialized_end=324
  _globals['_LISTNOTIFICATIONSREQUEST']._serialized_start=326
  _globals['_LISTNOTIFICATIONSREQUEST']._serialized_end=369
  _globals['_LISTNOTIFICATIONSRESPONSE']._serialized_start=371
  _globals['_LISTNOTIFICATIONSRESPONSE']._serialized_end=436
  _globals['_MARKASREADREQUEST']._serialized_start=438
  _globals['_MARKASREADREQUEST']._serialized_end=482
  _globals['_MARKASREADRESPONSE']._serialized_start=484
  _globals['_MARKASREADRESPONSE']._serialized_end=521
  _globals['_NOTIFICATIONS']._serialized_start=524
  _globals['_NOTIFICATIONS']._serialized_end=813
# @@protoc_insertion_point(module_scope)
