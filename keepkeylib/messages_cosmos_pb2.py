# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages-cosmos.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import types_pb2 as types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='messages-cosmos.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x15messages-cosmos.proto\x1a\x0btypes.proto\";\n\x10\x43osmosGetAddress\x12\x11\n\taddress_n\x18\x01 \x03(\r\x12\x14\n\x0cshow_display\x18\x02 \x01(\x08\" \n\rCosmosAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"\xa1\x01\n\x0c\x43osmosSignTx\x12\x11\n\taddress_n\x18\x01 \x03(\r\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x02 \x02(\x04\x12\x10\n\x08\x63hain_id\x18\x03 \x02(\t\x12\x17\n\x03\x66\x65\x65\x18\x04 \x02(\x0b\x32\n.CosmosFee\x12\x1b\n\x03msg\x18\x05 \x02(\x0b\x32\x0e.CosmosMsgSend\x12\x0c\n\x04memo\x18\x06 \x02(\t\x12\x10\n\x08sequence\x18\x07 \x02(\x04\"I\n\rCosmosMsgSend\x12\x14\n\x0c\x66rom_address\x18\x01 \x02(\t\x12\x12\n\nto_address\x18\x02 \x02(\t\x12\x0e\n\x06\x61mount\x18\x03 \x02(\x04\"(\n\tCosmosFee\x12\x0e\n\x06\x61mount\x18\x01 \x02(\r\x12\x0b\n\x03gas\x18\x02 \x02(\r\"7\n\x0e\x43osmosSignedTx\x12\x12\n\npublic_key\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x42\x32\n\x1a\x63om.keepkey.deviceprotocolB\x14KeepKeyMessageCosmos')
  ,
  dependencies=[types__pb2.DESCRIPTOR,])




_COSMOSGETADDRESS = _descriptor.Descriptor(
  name='CosmosGetAddress',
  full_name='CosmosGetAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address_n', full_name='CosmosGetAddress.address_n', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_display', full_name='CosmosGetAddress.show_display', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=97,
)


_COSMOSADDRESS = _descriptor.Descriptor(
  name='CosmosAddress',
  full_name='CosmosAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='CosmosAddress.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=131,
)


_COSMOSSIGNTX = _descriptor.Descriptor(
  name='CosmosSignTx',
  full_name='CosmosSignTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address_n', full_name='CosmosSignTx.address_n', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_number', full_name='CosmosSignTx.account_number', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain_id', full_name='CosmosSignTx.chain_id', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee', full_name='CosmosSignTx.fee', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='CosmosSignTx.msg', index=4,
      number=5, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='memo', full_name='CosmosSignTx.memo', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='CosmosSignTx.sequence', index=6,
      number=7, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=134,
  serialized_end=295,
)


_COSMOSMSGSEND = _descriptor.Descriptor(
  name='CosmosMsgSend',
  full_name='CosmosMsgSend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_address', full_name='CosmosMsgSend.from_address', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to_address', full_name='CosmosMsgSend.to_address', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='CosmosMsgSend.amount', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=297,
  serialized_end=370,
)


_COSMOSFEE = _descriptor.Descriptor(
  name='CosmosFee',
  full_name='CosmosFee',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='CosmosFee.amount', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas', full_name='CosmosFee.gas', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=372,
  serialized_end=412,
)


_COSMOSSIGNEDTX = _descriptor.Descriptor(
  name='CosmosSignedTx',
  full_name='CosmosSignedTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='public_key', full_name='CosmosSignedTx.public_key', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='CosmosSignedTx.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=414,
  serialized_end=469,
)

_COSMOSSIGNTX.fields_by_name['fee'].message_type = _COSMOSFEE
_COSMOSSIGNTX.fields_by_name['msg'].message_type = _COSMOSMSGSEND
DESCRIPTOR.message_types_by_name['CosmosGetAddress'] = _COSMOSGETADDRESS
DESCRIPTOR.message_types_by_name['CosmosAddress'] = _COSMOSADDRESS
DESCRIPTOR.message_types_by_name['CosmosSignTx'] = _COSMOSSIGNTX
DESCRIPTOR.message_types_by_name['CosmosMsgSend'] = _COSMOSMSGSEND
DESCRIPTOR.message_types_by_name['CosmosFee'] = _COSMOSFEE
DESCRIPTOR.message_types_by_name['CosmosSignedTx'] = _COSMOSSIGNEDTX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CosmosGetAddress = _reflection.GeneratedProtocolMessageType('CosmosGetAddress', (_message.Message,), dict(
  DESCRIPTOR = _COSMOSGETADDRESS,
  __module__ = 'messages_cosmos_pb2'
  # @@protoc_insertion_point(class_scope:CosmosGetAddress)
  ))
_sym_db.RegisterMessage(CosmosGetAddress)

CosmosAddress = _reflection.GeneratedProtocolMessageType('CosmosAddress', (_message.Message,), dict(
  DESCRIPTOR = _COSMOSADDRESS,
  __module__ = 'messages_cosmos_pb2'
  # @@protoc_insertion_point(class_scope:CosmosAddress)
  ))
_sym_db.RegisterMessage(CosmosAddress)

CosmosSignTx = _reflection.GeneratedProtocolMessageType('CosmosSignTx', (_message.Message,), dict(
  DESCRIPTOR = _COSMOSSIGNTX,
  __module__ = 'messages_cosmos_pb2'
  # @@protoc_insertion_point(class_scope:CosmosSignTx)
  ))
_sym_db.RegisterMessage(CosmosSignTx)

CosmosMsgSend = _reflection.GeneratedProtocolMessageType('CosmosMsgSend', (_message.Message,), dict(
  DESCRIPTOR = _COSMOSMSGSEND,
  __module__ = 'messages_cosmos_pb2'
  # @@protoc_insertion_point(class_scope:CosmosMsgSend)
  ))
_sym_db.RegisterMessage(CosmosMsgSend)

CosmosFee = _reflection.GeneratedProtocolMessageType('CosmosFee', (_message.Message,), dict(
  DESCRIPTOR = _COSMOSFEE,
  __module__ = 'messages_cosmos_pb2'
  # @@protoc_insertion_point(class_scope:CosmosFee)
  ))
_sym_db.RegisterMessage(CosmosFee)

CosmosSignedTx = _reflection.GeneratedProtocolMessageType('CosmosSignedTx', (_message.Message,), dict(
  DESCRIPTOR = _COSMOSSIGNEDTX,
  __module__ = 'messages_cosmos_pb2'
  # @@protoc_insertion_point(class_scope:CosmosSignedTx)
  ))
_sym_db.RegisterMessage(CosmosSignedTx)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.keepkey.deviceprotocolB\024KeepKeyMessageCosmos'))
# @@protoc_insertion_point(module_scope)
