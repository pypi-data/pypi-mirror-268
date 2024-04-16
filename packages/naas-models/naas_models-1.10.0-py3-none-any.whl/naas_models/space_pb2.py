# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: space.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bspace.proto\x12\x05space\x1a\x0evalidate.proto\"\x92\x03\n\tContainer\x12/\n\x04name\x18\x01 \x01(\tB\x1c\xfa\x42\x19r\x17\x10\x01\x18?2\x11^([A-Za-z0-9-]+)$H\x00\x88\x01\x01\x12J\n\x05image\x18\x02 \x01(\tB6\xfa\x42\x33r1\x10\x01\x32*^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$\xd0\x01\x00H\x01\x88\x01\x01\x12&\n\x03\x65nv\x18\x03 \x03(\x0b\x32\x19.space.Container.EnvEntry\x12\x1e\n\x04port\x18\x04 \x01(\x03\x42\x0b\xfa\x42\x08\"\x06\x18\xff\xff\x03(\x00H\x02\x88\x01\x01\x12\x32\n\x03\x63pu\x18\x05 \x01(\tB \xfa\x42\x1dr\x1b\x32\x16^[0-9]+(.[0-9]+)?[m]?$\xd0\x01\x00H\x03\x88\x01\x01\x12\x31\n\x06memory\x18\x06 \x01(\tB\x1c\xfa\x42\x19r\x17\x32\x12^[0-9]+(Mi|Gi|Ki)$\xd0\x01\x00H\x04\x88\x01\x01\x1a*\n\x08\x45nvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x07\n\x05_nameB\x08\n\x06_imageB\x07\n\x05_portB\x06\n\x04_cpuB\t\n\x07_memory\"\x9e\x03\n\x0f\x43ontainerUpdate\x12/\n\x04name\x18\x01 \x01(\tB\x1c\xfa\x42\x19r\x17\x10\x01\x18?2\x11^([A-Za-z0-9-]+)$H\x00\x88\x01\x01\x12J\n\x05image\x18\x02 \x01(\tB6\xfa\x42\x33r1\x10\x01\x32*^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$\xd0\x01\x00H\x01\x88\x01\x01\x12,\n\x03\x65nv\x18\x03 \x03(\x0b\x32\x1f.space.ContainerUpdate.EnvEntry\x12\x1e\n\x04port\x18\x04 \x01(\x03\x42\x0b\xfa\x42\x08\"\x06\x18\xff\xff\x03(\x00H\x02\x88\x01\x01\x12\x32\n\x03\x63pu\x18\x05 \x01(\tB \xfa\x42\x1dr\x1b\x32\x16^[0-9]+(.[0-9]+)?[m]?$\xd0\x01\x00H\x03\x88\x01\x01\x12\x31\n\x06memory\x18\x06 \x01(\tB\x1c\xfa\x42\x19r\x17\x32\x12^[0-9]+(Mi|Gi|Ki)$\xd0\x01\x00H\x04\x88\x01\x01\x1a*\n\x08\x45nvEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x07\n\x05_nameB\x08\n\x06_imageB\x07\n\x05_portB\x06\n\x04_cpuB\t\n\x07_memory\"\xf8\x01\n\x05Space\x12>\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$H\x00\x88\x01\x01\x12\x1e\n\x07user_id\x18\x02 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x01\x88\x01\x01\x12\x19\n\x02id\x18\x03 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01H\x02\x88\x01\x01\x12\x1d\n\x06\x64omain\x18\x04 \x01(\tB\x08\xfa\x42\x05r\x03\x90\x01\x01H\x03\x88\x01\x01\x12.\n\ncontainers\x18\x05 \x03(\x0b\x32\x10.space.ContainerB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x42\x07\n\x05_nameB\n\n\x08_user_idB\x05\n\x03_idB\t\n\x07_domain\"m\n\x0bSpaceUpdate\x12\x1d\n\x06\x64omain\x18\x04 \x01(\tB\x08\xfa\x42\x05r\x03\x90\x01\x01H\x00\x88\x01\x01\x12\x34\n\ncontainers\x18\x05 \x03(\x0b\x32\x16.space.ContainerUpdateB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x42\t\n\x07_domain\"\xa5\x01\n\x12SpaceResponseError\x12$\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x11.space.SpaceErrorH\x00\x88\x01\x01\x12\x13\n\x06status\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x13\n\x06reason\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x14\n\x07message\x18\x04 \x01(\tH\x03\x88\x01\x01\x42\x07\n\x05_codeB\t\n\x07_statusB\t\n\x07_reasonB\n\n\x08_message\"\xb9\x01\n\x14SpaceCreationRequest\x12>\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$H\x00\x88\x01\x01\x12\x1d\n\x06\x64omain\x18\x04 \x01(\tB\x08\xfa\x42\x05r\x03\x90\x01\x01H\x01\x88\x01\x01\x12.\n\ncontainers\x18\x05 \x03(\x0b\x32\x10.space.ContainerB\x08\xfa\x42\x05\x92\x01\x02\x08\x01\x42\x07\n\x05_nameB\t\n\x07_domain\"c\n\x15SpaceCreationResponse\x12 \n\x05space\x18\x01 \x01(\x0b\x32\x0c.space.SpaceH\x00\x88\x01\x01\x12\x13\n\x06status\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_spaceB\t\n\x07_status\"Z\n\x0fSpaceGetRequest\x12>\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$H\x00\x88\x01\x01\x42\x07\n\x05_name\"^\n\x10SpaceGetResponse\x12 \n\x05space\x18\x01 \x01(\x0b\x32\x0c.space.SpaceH\x00\x88\x01\x01\x12\x13\n\x06status\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_spaceB\t\n\x07_status\"_\n\x14SpaceDeletionRequest\x12>\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$H\x00\x88\x01\x01\x42\x07\n\x05_name\"7\n\x15SpaceDeletionResponse\x12\x13\n\x06status\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_status\"b\n\x10SpaceListRequest\x12\x16\n\tpage_size\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x18\n\x0bpage_number\x18\x02 \x01(\x05H\x01\x88\x01\x01\x42\x0c\n\n_page_sizeB\x0e\n\x0c_page_number\"1\n\x11SpaceListResponse\x12\x1c\n\x06spaces\x18\x01 \x03(\x0b\x32\x0c.space.Space\"\x8f\x01\n\x12SpaceUpdateRequest\x12>\n\x04name\x18\x01 \x01(\tB+\xfa\x42(r&\x10\x01\x18?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$H\x00\x88\x01\x01\x12&\n\x05space\x18\x02 \x01(\x0b\x32\x12.space.SpaceUpdateH\x01\x88\x01\x01\x42\x07\n\x05_nameB\x08\n\x06_space\"a\n\x13SpaceUpdateResponse\x12 \n\x05space\x18\x01 \x01(\x0b\x32\x0c.space.SpaceH\x00\x88\x01\x01\x12\x13\n\x06status\x18\x02 \x01(\tH\x01\x88\x01\x01\x42\x08\n\x06_spaceB\t\n\x07_status*\x8e\x01\n\nSpaceError\x12\x12\n\x0eSPACE_NO_ERROR\x10\x00\x12\x18\n\x14SPACE_ALREADY_EXISTS\x10\x01\x12\x13\n\x0fSPACE_NOT_FOUND\x10\x02\x12\x15\n\x11SPACE_NOT_UPDATED\x10\x03\x12&\n\"SPACE_MUST_HAVE_ONE_CONTAINER_PORT\x10\x04\x42.Z,github.com/jupyter-naas/naas-models/go/spaceb\x06proto3')

_SPACEERROR = DESCRIPTOR.enum_types_by_name['SpaceError']
SpaceError = enum_type_wrapper.EnumTypeWrapper(_SPACEERROR)
SPACE_NO_ERROR = 0
SPACE_ALREADY_EXISTS = 1
SPACE_NOT_FOUND = 2
SPACE_NOT_UPDATED = 3
SPACE_MUST_HAVE_ONE_CONTAINER_PORT = 4


_CONTAINER = DESCRIPTOR.message_types_by_name['Container']
_CONTAINER_ENVENTRY = _CONTAINER.nested_types_by_name['EnvEntry']
_CONTAINERUPDATE = DESCRIPTOR.message_types_by_name['ContainerUpdate']
_CONTAINERUPDATE_ENVENTRY = _CONTAINERUPDATE.nested_types_by_name['EnvEntry']
_SPACE = DESCRIPTOR.message_types_by_name['Space']
_SPACEUPDATE = DESCRIPTOR.message_types_by_name['SpaceUpdate']
_SPACERESPONSEERROR = DESCRIPTOR.message_types_by_name['SpaceResponseError']
_SPACECREATIONREQUEST = DESCRIPTOR.message_types_by_name['SpaceCreationRequest']
_SPACECREATIONRESPONSE = DESCRIPTOR.message_types_by_name['SpaceCreationResponse']
_SPACEGETREQUEST = DESCRIPTOR.message_types_by_name['SpaceGetRequest']
_SPACEGETRESPONSE = DESCRIPTOR.message_types_by_name['SpaceGetResponse']
_SPACEDELETIONREQUEST = DESCRIPTOR.message_types_by_name['SpaceDeletionRequest']
_SPACEDELETIONRESPONSE = DESCRIPTOR.message_types_by_name['SpaceDeletionResponse']
_SPACELISTREQUEST = DESCRIPTOR.message_types_by_name['SpaceListRequest']
_SPACELISTRESPONSE = DESCRIPTOR.message_types_by_name['SpaceListResponse']
_SPACEUPDATEREQUEST = DESCRIPTOR.message_types_by_name['SpaceUpdateRequest']
_SPACEUPDATERESPONSE = DESCRIPTOR.message_types_by_name['SpaceUpdateResponse']
Container = _reflection.GeneratedProtocolMessageType('Container', (_message.Message,), {

  'EnvEntry' : _reflection.GeneratedProtocolMessageType('EnvEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONTAINER_ENVENTRY,
    '__module__' : 'space_pb2'
    # @@protoc_insertion_point(class_scope:space.Container.EnvEntry)
    })
  ,
  'DESCRIPTOR' : _CONTAINER,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.Container)
  })
_sym_db.RegisterMessage(Container)
_sym_db.RegisterMessage(Container.EnvEntry)

ContainerUpdate = _reflection.GeneratedProtocolMessageType('ContainerUpdate', (_message.Message,), {

  'EnvEntry' : _reflection.GeneratedProtocolMessageType('EnvEntry', (_message.Message,), {
    'DESCRIPTOR' : _CONTAINERUPDATE_ENVENTRY,
    '__module__' : 'space_pb2'
    # @@protoc_insertion_point(class_scope:space.ContainerUpdate.EnvEntry)
    })
  ,
  'DESCRIPTOR' : _CONTAINERUPDATE,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.ContainerUpdate)
  })
_sym_db.RegisterMessage(ContainerUpdate)
_sym_db.RegisterMessage(ContainerUpdate.EnvEntry)

Space = _reflection.GeneratedProtocolMessageType('Space', (_message.Message,), {
  'DESCRIPTOR' : _SPACE,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.Space)
  })
_sym_db.RegisterMessage(Space)

SpaceUpdate = _reflection.GeneratedProtocolMessageType('SpaceUpdate', (_message.Message,), {
  'DESCRIPTOR' : _SPACEUPDATE,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceUpdate)
  })
_sym_db.RegisterMessage(SpaceUpdate)

SpaceResponseError = _reflection.GeneratedProtocolMessageType('SpaceResponseError', (_message.Message,), {
  'DESCRIPTOR' : _SPACERESPONSEERROR,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceResponseError)
  })
_sym_db.RegisterMessage(SpaceResponseError)

SpaceCreationRequest = _reflection.GeneratedProtocolMessageType('SpaceCreationRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPACECREATIONREQUEST,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceCreationRequest)
  })
_sym_db.RegisterMessage(SpaceCreationRequest)

SpaceCreationResponse = _reflection.GeneratedProtocolMessageType('SpaceCreationResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPACECREATIONRESPONSE,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceCreationResponse)
  })
_sym_db.RegisterMessage(SpaceCreationResponse)

SpaceGetRequest = _reflection.GeneratedProtocolMessageType('SpaceGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPACEGETREQUEST,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceGetRequest)
  })
_sym_db.RegisterMessage(SpaceGetRequest)

SpaceGetResponse = _reflection.GeneratedProtocolMessageType('SpaceGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPACEGETRESPONSE,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceGetResponse)
  })
_sym_db.RegisterMessage(SpaceGetResponse)

SpaceDeletionRequest = _reflection.GeneratedProtocolMessageType('SpaceDeletionRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPACEDELETIONREQUEST,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceDeletionRequest)
  })
_sym_db.RegisterMessage(SpaceDeletionRequest)

SpaceDeletionResponse = _reflection.GeneratedProtocolMessageType('SpaceDeletionResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPACEDELETIONRESPONSE,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceDeletionResponse)
  })
_sym_db.RegisterMessage(SpaceDeletionResponse)

SpaceListRequest = _reflection.GeneratedProtocolMessageType('SpaceListRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPACELISTREQUEST,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceListRequest)
  })
_sym_db.RegisterMessage(SpaceListRequest)

SpaceListResponse = _reflection.GeneratedProtocolMessageType('SpaceListResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPACELISTRESPONSE,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceListResponse)
  })
_sym_db.RegisterMessage(SpaceListResponse)

SpaceUpdateRequest = _reflection.GeneratedProtocolMessageType('SpaceUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _SPACEUPDATEREQUEST,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceUpdateRequest)
  })
_sym_db.RegisterMessage(SpaceUpdateRequest)

SpaceUpdateResponse = _reflection.GeneratedProtocolMessageType('SpaceUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _SPACEUPDATERESPONSE,
  '__module__' : 'space_pb2'
  # @@protoc_insertion_point(class_scope:space.SpaceUpdateResponse)
  })
_sym_db.RegisterMessage(SpaceUpdateResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/jupyter-naas/naas-models/go/space'
  _CONTAINER_ENVENTRY._options = None
  _CONTAINER_ENVENTRY._serialized_options = b'8\001'
  _CONTAINER.fields_by_name['name']._options = None
  _CONTAINER.fields_by_name['name']._serialized_options = b'\372B\031r\027\020\001\030?2\021^([A-Za-z0-9-]+)$'
  _CONTAINER.fields_by_name['image']._options = None
  _CONTAINER.fields_by_name['image']._serialized_options = b'\372B3r1\020\0012*^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$\320\001\000'
  _CONTAINER.fields_by_name['port']._options = None
  _CONTAINER.fields_by_name['port']._serialized_options = b'\372B\010\"\006\030\377\377\003(\000'
  _CONTAINER.fields_by_name['cpu']._options = None
  _CONTAINER.fields_by_name['cpu']._serialized_options = b'\372B\035r\0332\026^[0-9]+(.[0-9]+)?[m]?$\320\001\000'
  _CONTAINER.fields_by_name['memory']._options = None
  _CONTAINER.fields_by_name['memory']._serialized_options = b'\372B\031r\0272\022^[0-9]+(Mi|Gi|Ki)$\320\001\000'
  _CONTAINERUPDATE_ENVENTRY._options = None
  _CONTAINERUPDATE_ENVENTRY._serialized_options = b'8\001'
  _CONTAINERUPDATE.fields_by_name['name']._options = None
  _CONTAINERUPDATE.fields_by_name['name']._serialized_options = b'\372B\031r\027\020\001\030?2\021^([A-Za-z0-9-]+)$'
  _CONTAINERUPDATE.fields_by_name['image']._options = None
  _CONTAINERUPDATE.fields_by_name['image']._serialized_options = b'\372B3r1\020\0012*^[a-zA-Z0-9\\.\\/-]+([:][a-zA-Z0-9\\.\\/-]*)?$\320\001\000'
  _CONTAINERUPDATE.fields_by_name['port']._options = None
  _CONTAINERUPDATE.fields_by_name['port']._serialized_options = b'\372B\010\"\006\030\377\377\003(\000'
  _CONTAINERUPDATE.fields_by_name['cpu']._options = None
  _CONTAINERUPDATE.fields_by_name['cpu']._serialized_options = b'\372B\035r\0332\026^[0-9]+(.[0-9]+)?[m]?$\320\001\000'
  _CONTAINERUPDATE.fields_by_name['memory']._options = None
  _CONTAINERUPDATE.fields_by_name['memory']._serialized_options = b'\372B\031r\0272\022^[0-9]+(Mi|Gi|Ki)$\320\001\000'
  _SPACE.fields_by_name['name']._options = None
  _SPACE.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$'
  _SPACE.fields_by_name['user_id']._options = None
  _SPACE.fields_by_name['user_id']._serialized_options = b'\372B\005r\003\260\001\001'
  _SPACE.fields_by_name['id']._options = None
  _SPACE.fields_by_name['id']._serialized_options = b'\372B\005r\003\260\001\001'
  _SPACE.fields_by_name['domain']._options = None
  _SPACE.fields_by_name['domain']._serialized_options = b'\372B\005r\003\220\001\001'
  _SPACE.fields_by_name['containers']._options = None
  _SPACE.fields_by_name['containers']._serialized_options = b'\372B\005\222\001\002\010\001'
  _SPACEUPDATE.fields_by_name['domain']._options = None
  _SPACEUPDATE.fields_by_name['domain']._serialized_options = b'\372B\005r\003\220\001\001'
  _SPACEUPDATE.fields_by_name['containers']._options = None
  _SPACEUPDATE.fields_by_name['containers']._serialized_options = b'\372B\005\222\001\002\010\001'
  _SPACECREATIONREQUEST.fields_by_name['name']._options = None
  _SPACECREATIONREQUEST.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$'
  _SPACECREATIONREQUEST.fields_by_name['domain']._options = None
  _SPACECREATIONREQUEST.fields_by_name['domain']._serialized_options = b'\372B\005r\003\220\001\001'
  _SPACECREATIONREQUEST.fields_by_name['containers']._options = None
  _SPACECREATIONREQUEST.fields_by_name['containers']._serialized_options = b'\372B\005\222\001\002\010\001'
  _SPACEGETREQUEST.fields_by_name['name']._options = None
  _SPACEGETREQUEST.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$'
  _SPACEDELETIONREQUEST.fields_by_name['name']._options = None
  _SPACEDELETIONREQUEST.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$'
  _SPACEUPDATEREQUEST.fields_by_name['name']._options = None
  _SPACEUPDATEREQUEST.fields_by_name['name']._serialized_options = b'\372B(r&\020\001\030?2 ^([A-Za-z0-9]+(-[A-Za-z0-9]+)+)$'
  _SPACEERROR._serialized_start=2418
  _SPACEERROR._serialized_end=2560
  _CONTAINER._serialized_start=39
  _CONTAINER._serialized_end=441
  _CONTAINER_ENVENTRY._serialized_start=352
  _CONTAINER_ENVENTRY._serialized_end=394
  _CONTAINERUPDATE._serialized_start=444
  _CONTAINERUPDATE._serialized_end=858
  _CONTAINERUPDATE_ENVENTRY._serialized_start=352
  _CONTAINERUPDATE_ENVENTRY._serialized_end=394
  _SPACE._serialized_start=861
  _SPACE._serialized_end=1109
  _SPACEUPDATE._serialized_start=1111
  _SPACEUPDATE._serialized_end=1220
  _SPACERESPONSEERROR._serialized_start=1223
  _SPACERESPONSEERROR._serialized_end=1388
  _SPACECREATIONREQUEST._serialized_start=1391
  _SPACECREATIONREQUEST._serialized_end=1576
  _SPACECREATIONRESPONSE._serialized_start=1578
  _SPACECREATIONRESPONSE._serialized_end=1677
  _SPACEGETREQUEST._serialized_start=1679
  _SPACEGETREQUEST._serialized_end=1769
  _SPACEGETRESPONSE._serialized_start=1771
  _SPACEGETRESPONSE._serialized_end=1865
  _SPACEDELETIONREQUEST._serialized_start=1867
  _SPACEDELETIONREQUEST._serialized_end=1962
  _SPACEDELETIONRESPONSE._serialized_start=1964
  _SPACEDELETIONRESPONSE._serialized_end=2019
  _SPACELISTREQUEST._serialized_start=2021
  _SPACELISTREQUEST._serialized_end=2119
  _SPACELISTRESPONSE._serialized_start=2121
  _SPACELISTRESPONSE._serialized_end=2170
  _SPACEUPDATEREQUEST._serialized_start=2173
  _SPACEUPDATEREQUEST._serialized_end=2316
  _SPACEUPDATERESPONSE._serialized_start=2318
  _SPACEUPDATERESPONSE._serialized_end=2415
# @@protoc_insertion_point(module_scope)
