# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: storage.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import naas_models.validate_pb2 as validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rstorage.proto\x12\x07storage\x1a\x0evalidate.proto\"%\n\x07Storage\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x07\n\x05_name\"\xa8\x01\n\x06Object\x12\x11\n\x04name\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04type\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06prefix\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x11\n\x04size\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x19\n\x0clastmodified\x18\x05 \x01(\tH\x04\x88\x01\x01\x42\x07\n\x05_nameB\x07\n\x05_typeB\t\n\x07_prefixB\x07\n\x05_sizeB\x0f\n\r_lastmodified\"m\n\x14StorageResponseError\x12)\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x15.storage.StorageErrorH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_errorB\n\n\x08_message\"k\n\x13ObjectResponseError\x12(\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x14.storage.ObjectErrorH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_errorB\n\n\x08_message\"\x82\x01\n%ObjectStorageCredentialsResponseError\x12-\n\x05\x65rror\x18\x01 \x01(\x0e\x32\x19.storage.CredentialsErrorH\x00\x88\x01\x01\x12\x14\n\x07message\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_errorB\n\n\x08_message\"y\n\x12StorageListRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12$\n\x06object\x18\x02 \x01(\x0b\x32\x0f.storage.ObjectH\x01\x88\x01\x01\x42\n\n\x08_storageB\t\n\x07_object\"u\n\x13StorageListResponse\x12!\n\x07storage\x18\x01 \x03(\x0b\x32\x10.storage.Storage\x12\x31\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"J\n\x14StorageCreateRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x42\n\n\x08_storage\"\x88\x01\n\x15StorageCreateResponse\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12\x31\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x01\x88\x01\x01\x42\n\n\x08_storageB\x08\n\x06_error\"J\n\x14StorageDeleteRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x42\n\n\x08_storage\"T\n\x15StorageDeleteResponse\x12\x31\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"\x7f\n\x18StorageListObjectRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12$\n\x06object\x18\x02 \x01(\x0b\x32\x0f.storage.ObjectH\x01\x88\x01\x01\x42\n\n\x08_storageB\t\n\x07_object\"y\n\x19StorageListObjectResponse\x12\x1f\n\x06object\x18\x01 \x03(\x0b\x32\x0f.storage.Object\x12\x31\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"z\n\x13ObjectCreateRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12$\n\x06object\x18\x02 \x01(\x0b\x32\x0f.storage.ObjectH\x01\x88\x01\x01\x42\n\n\x08_storageB\t\n\x07_object\"S\n\x14ObjectCreateResponse\x12\x31\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1d.storage.StorageResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"x\n\x11ObjectListRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12$\n\x06object\x18\x02 \x01(\x0b\x32\x0f.storage.ObjectH\x01\x88\x01\x01\x42\n\n\x08_storageB\t\n\x07_object\"q\n\x12ObjectListResponse\x12\x1f\n\x06object\x18\x01 \x03(\x0b\x32\x0f.storage.Object\x12\x30\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.storage.ObjectResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"w\n\x10ObjectGetRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x12$\n\x06object\x18\x02 \x01(\x0b\x32\x0f.storage.ObjectH\x01\x88\x01\x01\x42\n\n\x08_storageB\t\n\x07_object\"\x80\x01\n\x11ObjectGetResponse\x12$\n\x06object\x18\x01 \x01(\x0b\x32\x0f.storage.ObjectH\x00\x88\x01\x01\x12\x30\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.storage.ObjectResponseErrorH\x01\x88\x01\x01\x42\t\n\x07_objectB\x08\n\x06_error\"F\n\x13ObjectDeleteRequest\x12$\n\x06object\x18\x01 \x01(\x0b\x32\x0f.storage.ObjectH\x00\x88\x01\x01\x42\t\n\x07_object\"R\n\x14ObjectDeleteResponse\x12\x30\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x1c.storage.ObjectResponseErrorH\x00\x88\x01\x01\x42\x08\n\x06_error\"\x9e\x02\n\x1aObjectStorageS3Credentials\x12\x19\n\x0c\x65ndpoint_url\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x18\n\x0bregion_name\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x1a\n\raccess_key_id\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x17\n\nsecret_key\x18\x04 \x01(\tH\x03\x88\x01\x01\x12\x1a\n\rsession_token\x18\x05 \x01(\tH\x04\x88\x01\x01\x12\x17\n\nexpiration\x18\x06 \x01(\tH\x05\x88\x01\x01\x42\x0f\n\r_endpoint_urlB\x0e\n\x0c_region_nameB\x10\n\x0e_access_key_idB\r\n\x0b_secret_keyB\x10\n\x0e_session_tokenB\r\n\x0b_expiration\"\xa1\x01\n\x1dObjectStorageAzureCredentials\x12\x19\n\x0c\x65ndpoint_url\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\raccess_key_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x17\n\nsecret_key\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\x0f\n\r_endpoint_urlB\x10\n\x0e_access_key_idB\r\n\x0b_secret_key\"K\n\x18ObjectStorageCredentials\x12/\n\x02s3\x18\x01 \x01(\x0b\x32#.storage.ObjectStorageS3Credentials\"U\n\x1fObjectStorageCredentialsRequest\x12&\n\x07storage\x18\x01 \x01(\x0b\x32\x10.storage.StorageH\x00\x88\x01\x01\x42\n\n\x08_storage\"\xbd\x01\n ObjectStorageCredentialsResponse\x12;\n\x0b\x63redentials\x18\x01 \x01(\x0b\x32!.storage.ObjectStorageCredentialsH\x00\x88\x01\x01\x12\x42\n\x05\x65rror\x18\x02 \x01(\x0b\x32..storage.ObjectStorageCredentialsResponseErrorH\x01\x88\x01\x01\x42\x0e\n\x0c_credentialsB\x08\n\x06_error*V\n\x0cStorageError\x12\x14\n\x10STORAGE_NO_ERROR\x10\x00\x12\x19\n\x15STORAGE_ALREADY_EXIST\x10\x01\x12\x15\n\x11STORAGE_NOT_FOUND\x10\x02*\x83\x01\n\x0bObjectError\x12\x13\n\x0fOBJECT_NO_ERROR\x10\x00\x12\x18\n\x14OBJECT_ALREADY_EXIST\x10\x01\x12\x15\n\x11OBJECT_SIZE_ERROR\x10\x02\x12\x14\n\x10OBJECT_NOT_FOUND\x10\x03\x12\x18\n\x14OBJECT_DIR_NOT_EMPTY\x10\x04*,\n\x10\x43redentialsError\x12\x18\n\x14\x43REDENTIALS_NO_ERROR\x10\x00\x42\x30Z.github.com/jupyter-naas/naas-models/go/storageb\x06proto3')

_STORAGEERROR = DESCRIPTOR.enum_types_by_name['StorageError']
StorageError = enum_type_wrapper.EnumTypeWrapper(_STORAGEERROR)
_OBJECTERROR = DESCRIPTOR.enum_types_by_name['ObjectError']
ObjectError = enum_type_wrapper.EnumTypeWrapper(_OBJECTERROR)
_CREDENTIALSERROR = DESCRIPTOR.enum_types_by_name['CredentialsError']
CredentialsError = enum_type_wrapper.EnumTypeWrapper(_CREDENTIALSERROR)
STORAGE_NO_ERROR = 0
STORAGE_ALREADY_EXIST = 1
STORAGE_NOT_FOUND = 2
OBJECT_NO_ERROR = 0
OBJECT_ALREADY_EXIST = 1
OBJECT_SIZE_ERROR = 2
OBJECT_NOT_FOUND = 3
OBJECT_DIR_NOT_EMPTY = 4
CREDENTIALS_NO_ERROR = 0


_STORAGE = DESCRIPTOR.message_types_by_name['Storage']
_OBJECT = DESCRIPTOR.message_types_by_name['Object']
_STORAGERESPONSEERROR = DESCRIPTOR.message_types_by_name['StorageResponseError']
_OBJECTRESPONSEERROR = DESCRIPTOR.message_types_by_name['ObjectResponseError']
_OBJECTSTORAGECREDENTIALSRESPONSEERROR = DESCRIPTOR.message_types_by_name['ObjectStorageCredentialsResponseError']
_STORAGELISTREQUEST = DESCRIPTOR.message_types_by_name['StorageListRequest']
_STORAGELISTRESPONSE = DESCRIPTOR.message_types_by_name['StorageListResponse']
_STORAGECREATEREQUEST = DESCRIPTOR.message_types_by_name['StorageCreateRequest']
_STORAGECREATERESPONSE = DESCRIPTOR.message_types_by_name['StorageCreateResponse']
_STORAGEDELETEREQUEST = DESCRIPTOR.message_types_by_name['StorageDeleteRequest']
_STORAGEDELETERESPONSE = DESCRIPTOR.message_types_by_name['StorageDeleteResponse']
_STORAGELISTOBJECTREQUEST = DESCRIPTOR.message_types_by_name['StorageListObjectRequest']
_STORAGELISTOBJECTRESPONSE = DESCRIPTOR.message_types_by_name['StorageListObjectResponse']
_OBJECTCREATEREQUEST = DESCRIPTOR.message_types_by_name['ObjectCreateRequest']
_OBJECTCREATERESPONSE = DESCRIPTOR.message_types_by_name['ObjectCreateResponse']
_OBJECTLISTREQUEST = DESCRIPTOR.message_types_by_name['ObjectListRequest']
_OBJECTLISTRESPONSE = DESCRIPTOR.message_types_by_name['ObjectListResponse']
_OBJECTGETREQUEST = DESCRIPTOR.message_types_by_name['ObjectGetRequest']
_OBJECTGETRESPONSE = DESCRIPTOR.message_types_by_name['ObjectGetResponse']
_OBJECTDELETEREQUEST = DESCRIPTOR.message_types_by_name['ObjectDeleteRequest']
_OBJECTDELETERESPONSE = DESCRIPTOR.message_types_by_name['ObjectDeleteResponse']
_OBJECTSTORAGES3CREDENTIALS = DESCRIPTOR.message_types_by_name['ObjectStorageS3Credentials']
_OBJECTSTORAGEAZURECREDENTIALS = DESCRIPTOR.message_types_by_name['ObjectStorageAzureCredentials']
_OBJECTSTORAGECREDENTIALS = DESCRIPTOR.message_types_by_name['ObjectStorageCredentials']
_OBJECTSTORAGECREDENTIALSREQUEST = DESCRIPTOR.message_types_by_name['ObjectStorageCredentialsRequest']
_OBJECTSTORAGECREDENTIALSRESPONSE = DESCRIPTOR.message_types_by_name['ObjectStorageCredentialsResponse']
Storage = _reflection.GeneratedProtocolMessageType('Storage', (_message.Message,), {
  'DESCRIPTOR' : _STORAGE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.Storage)
  })
_sym_db.RegisterMessage(Storage)

Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), {
  'DESCRIPTOR' : _OBJECT,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.Object)
  })
_sym_db.RegisterMessage(Object)

StorageResponseError = _reflection.GeneratedProtocolMessageType('StorageResponseError', (_message.Message,), {
  'DESCRIPTOR' : _STORAGERESPONSEERROR,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageResponseError)
  })
_sym_db.RegisterMessage(StorageResponseError)

ObjectResponseError = _reflection.GeneratedProtocolMessageType('ObjectResponseError', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTRESPONSEERROR,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectResponseError)
  })
_sym_db.RegisterMessage(ObjectResponseError)

ObjectStorageCredentialsResponseError = _reflection.GeneratedProtocolMessageType('ObjectStorageCredentialsResponseError', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSTORAGECREDENTIALSRESPONSEERROR,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectStorageCredentialsResponseError)
  })
_sym_db.RegisterMessage(ObjectStorageCredentialsResponseError)

StorageListRequest = _reflection.GeneratedProtocolMessageType('StorageListRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGELISTREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageListRequest)
  })
_sym_db.RegisterMessage(StorageListRequest)

StorageListResponse = _reflection.GeneratedProtocolMessageType('StorageListResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORAGELISTRESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageListResponse)
  })
_sym_db.RegisterMessage(StorageListResponse)

StorageCreateRequest = _reflection.GeneratedProtocolMessageType('StorageCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGECREATEREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageCreateRequest)
  })
_sym_db.RegisterMessage(StorageCreateRequest)

StorageCreateResponse = _reflection.GeneratedProtocolMessageType('StorageCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORAGECREATERESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageCreateResponse)
  })
_sym_db.RegisterMessage(StorageCreateResponse)

StorageDeleteRequest = _reflection.GeneratedProtocolMessageType('StorageDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGEDELETEREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageDeleteRequest)
  })
_sym_db.RegisterMessage(StorageDeleteRequest)

StorageDeleteResponse = _reflection.GeneratedProtocolMessageType('StorageDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORAGEDELETERESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageDeleteResponse)
  })
_sym_db.RegisterMessage(StorageDeleteResponse)

StorageListObjectRequest = _reflection.GeneratedProtocolMessageType('StorageListObjectRequest', (_message.Message,), {
  'DESCRIPTOR' : _STORAGELISTOBJECTREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageListObjectRequest)
  })
_sym_db.RegisterMessage(StorageListObjectRequest)

StorageListObjectResponse = _reflection.GeneratedProtocolMessageType('StorageListObjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _STORAGELISTOBJECTRESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.StorageListObjectResponse)
  })
_sym_db.RegisterMessage(StorageListObjectResponse)

ObjectCreateRequest = _reflection.GeneratedProtocolMessageType('ObjectCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTCREATEREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectCreateRequest)
  })
_sym_db.RegisterMessage(ObjectCreateRequest)

ObjectCreateResponse = _reflection.GeneratedProtocolMessageType('ObjectCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTCREATERESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectCreateResponse)
  })
_sym_db.RegisterMessage(ObjectCreateResponse)

ObjectListRequest = _reflection.GeneratedProtocolMessageType('ObjectListRequest', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTLISTREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectListRequest)
  })
_sym_db.RegisterMessage(ObjectListRequest)

ObjectListResponse = _reflection.GeneratedProtocolMessageType('ObjectListResponse', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTLISTRESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectListResponse)
  })
_sym_db.RegisterMessage(ObjectListResponse)

ObjectGetRequest = _reflection.GeneratedProtocolMessageType('ObjectGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTGETREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectGetRequest)
  })
_sym_db.RegisterMessage(ObjectGetRequest)

ObjectGetResponse = _reflection.GeneratedProtocolMessageType('ObjectGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTGETRESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectGetResponse)
  })
_sym_db.RegisterMessage(ObjectGetResponse)

ObjectDeleteRequest = _reflection.GeneratedProtocolMessageType('ObjectDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTDELETEREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectDeleteRequest)
  })
_sym_db.RegisterMessage(ObjectDeleteRequest)

ObjectDeleteResponse = _reflection.GeneratedProtocolMessageType('ObjectDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTDELETERESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectDeleteResponse)
  })
_sym_db.RegisterMessage(ObjectDeleteResponse)

ObjectStorageS3Credentials = _reflection.GeneratedProtocolMessageType('ObjectStorageS3Credentials', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSTORAGES3CREDENTIALS,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectStorageS3Credentials)
  })
_sym_db.RegisterMessage(ObjectStorageS3Credentials)

ObjectStorageAzureCredentials = _reflection.GeneratedProtocolMessageType('ObjectStorageAzureCredentials', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSTORAGEAZURECREDENTIALS,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectStorageAzureCredentials)
  })
_sym_db.RegisterMessage(ObjectStorageAzureCredentials)

ObjectStorageCredentials = _reflection.GeneratedProtocolMessageType('ObjectStorageCredentials', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSTORAGECREDENTIALS,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectStorageCredentials)
  })
_sym_db.RegisterMessage(ObjectStorageCredentials)

ObjectStorageCredentialsRequest = _reflection.GeneratedProtocolMessageType('ObjectStorageCredentialsRequest', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSTORAGECREDENTIALSREQUEST,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectStorageCredentialsRequest)
  })
_sym_db.RegisterMessage(ObjectStorageCredentialsRequest)

ObjectStorageCredentialsResponse = _reflection.GeneratedProtocolMessageType('ObjectStorageCredentialsResponse', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTSTORAGECREDENTIALSRESPONSE,
  '__module__' : 'storage_pb2'
  # @@protoc_insertion_point(class_scope:storage.ObjectStorageCredentialsResponse)
  })
_sym_db.RegisterMessage(ObjectStorageCredentialsResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z.github.com/jupyter-naas/naas-models/go/storage'
  _STORAGEERROR._serialized_start=3139
  _STORAGEERROR._serialized_end=3225
  _OBJECTERROR._serialized_start=3228
  _OBJECTERROR._serialized_end=3359
  _CREDENTIALSERROR._serialized_start=3361
  _CREDENTIALSERROR._serialized_end=3405
  _STORAGE._serialized_start=42
  _STORAGE._serialized_end=79
  _OBJECT._serialized_start=82
  _OBJECT._serialized_end=250
  _STORAGERESPONSEERROR._serialized_start=252
  _STORAGERESPONSEERROR._serialized_end=361
  _OBJECTRESPONSEERROR._serialized_start=363
  _OBJECTRESPONSEERROR._serialized_end=470
  _OBJECTSTORAGECREDENTIALSRESPONSEERROR._serialized_start=473
  _OBJECTSTORAGECREDENTIALSRESPONSEERROR._serialized_end=603
  _STORAGELISTREQUEST._serialized_start=605
  _STORAGELISTREQUEST._serialized_end=726
  _STORAGELISTRESPONSE._serialized_start=728
  _STORAGELISTRESPONSE._serialized_end=845
  _STORAGECREATEREQUEST._serialized_start=847
  _STORAGECREATEREQUEST._serialized_end=921
  _STORAGECREATERESPONSE._serialized_start=924
  _STORAGECREATERESPONSE._serialized_end=1060
  _STORAGEDELETEREQUEST._serialized_start=1062
  _STORAGEDELETEREQUEST._serialized_end=1136
  _STORAGEDELETERESPONSE._serialized_start=1138
  _STORAGEDELETERESPONSE._serialized_end=1222
  _STORAGELISTOBJECTREQUEST._serialized_start=1224
  _STORAGELISTOBJECTREQUEST._serialized_end=1351
  _STORAGELISTOBJECTRESPONSE._serialized_start=1353
  _STORAGELISTOBJECTRESPONSE._serialized_end=1474
  _OBJECTCREATEREQUEST._serialized_start=1476
  _OBJECTCREATEREQUEST._serialized_end=1598
  _OBJECTCREATERESPONSE._serialized_start=1600
  _OBJECTCREATERESPONSE._serialized_end=1683
  _OBJECTLISTREQUEST._serialized_start=1685
  _OBJECTLISTREQUEST._serialized_end=1805
  _OBJECTLISTRESPONSE._serialized_start=1807
  _OBJECTLISTRESPONSE._serialized_end=1920
  _OBJECTGETREQUEST._serialized_start=1922
  _OBJECTGETREQUEST._serialized_end=2041
  _OBJECTGETRESPONSE._serialized_start=2044
  _OBJECTGETRESPONSE._serialized_end=2172
  _OBJECTDELETEREQUEST._serialized_start=2174
  _OBJECTDELETEREQUEST._serialized_end=2244
  _OBJECTDELETERESPONSE._serialized_start=2246
  _OBJECTDELETERESPONSE._serialized_end=2328
  _OBJECTSTORAGES3CREDENTIALS._serialized_start=2331
  _OBJECTSTORAGES3CREDENTIALS._serialized_end=2617
  _OBJECTSTORAGEAZURECREDENTIALS._serialized_start=2620
  _OBJECTSTORAGEAZURECREDENTIALS._serialized_end=2781
  _OBJECTSTORAGECREDENTIALS._serialized_start=2783
  _OBJECTSTORAGECREDENTIALS._serialized_end=2858
  _OBJECTSTORAGECREDENTIALSREQUEST._serialized_start=2860
  _OBJECTSTORAGECREDENTIALSREQUEST._serialized_end=2945
  _OBJECTSTORAGECREDENTIALSRESPONSE._serialized_start=2948
  _OBJECTSTORAGECREDENTIALSRESPONSE._serialized_end=3137
# @@protoc_insertion_point(module_scope)
