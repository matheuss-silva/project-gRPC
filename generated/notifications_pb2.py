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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13notifications.proto\x12\rnotifications\"H\n\x0cNotification\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0c\n\x04read\x18\x04 \x01(\x08\"+\n\x18ListNotificationsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"O\n\x19ListNotificationsResponse\x12\x32\n\rnotifications\x18\x01 \x03(\x0b\x32\x1b.notifications.Notification\",\n\x11MarkAsReadRequest\x12\x17\n\x0fnotification_id\x18\x01 \x01(\t\"%\n\x12MarkAsReadResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xaa\x02\n\rNotifications\x12R\n\x10SendNotification\x12\x1b.notifications.Notification\x1a!.notifications.MarkAsReadResponse\x12\x66\n\x11ListNotifications\x12\'.notifications.ListNotificationsRequest\x1a(.notifications.ListNotificationsResponse\x12]\n\x16MarkNotificationAsRead\x12 .notifications.MarkAsReadRequest\x1a!.notifications.MarkAsReadResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'notifications_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_NOTIFICATION']._serialized_start=38
  _globals['_NOTIFICATION']._serialized_end=110
  _globals['_LISTNOTIFICATIONSREQUEST']._serialized_start=112
  _globals['_LISTNOTIFICATIONSREQUEST']._serialized_end=155
  _globals['_LISTNOTIFICATIONSRESPONSE']._serialized_start=157
  _globals['_LISTNOTIFICATIONSRESPONSE']._serialized_end=236
  _globals['_MARKASREADREQUEST']._serialized_start=238
  _globals['_MARKASREADREQUEST']._serialized_end=282
  _globals['_MARKASREADRESPONSE']._serialized_start=284
  _globals['_MARKASREADRESPONSE']._serialized_end=321
  _globals['_NOTIFICATIONS']._serialized_start=324
  _globals['_NOTIFICATIONS']._serialized_end=622
# @@protoc_insertion_point(module_scope)
