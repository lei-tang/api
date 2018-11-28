# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/filter/http/jwt_auth/v2alpha1/config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='envoy/config/filter/http/jwt_auth/v2alpha1/config.proto',
  package='istio.envoy.config.filter.http.jwt_auth.v2alpha1',
  syntax='proto3',
  serialized_pb=_b('\n7envoy/config/filter/http/jwt_auth/v2alpha1/config.proto\x12\x30istio.envoy.config.filter.http.jwt_auth.v2alpha1\x1a\x1egoogle/protobuf/duration.proto\"k\n\x07HttpUri\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x11\n\x07\x63luster\x18\x02 \x01(\tH\x00\x12*\n\x07timeout\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationB\x14\n\x12http_upstream_type\"^\n\nDataSource\x12\x12\n\x08\x66ilename\x18\x01 \x01(\tH\x00\x12\x16\n\x0cinline_bytes\x18\x02 \x01(\x0cH\x00\x12\x17\n\rinline_string\x18\x03 \x01(\tH\x00\x42\x0b\n\tspecifier\"\x87\x03\n\x07JwtRule\x12\x0e\n\x06issuer\x18\x01 \x01(\t\x12\x11\n\taudiences\x18\x02 \x03(\t\x12S\n\x0bremote_jwks\x18\x03 \x01(\x0b\x32<.istio.envoy.config.filter.http.jwt_auth.v2alpha1.RemoteJwksH\x00\x12R\n\nlocal_jwks\x18\x04 \x01(\x0b\x32<.istio.envoy.config.filter.http.jwt_auth.v2alpha1.DataSourceH\x00\x12\x0f\n\x07\x66orward\x18\x05 \x01(\x08\x12Q\n\x0c\x66rom_headers\x18\x06 \x03(\x0b\x32;.istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtHeader\x12\x13\n\x0b\x66rom_params\x18\x07 \x03(\t\x12\x1e\n\x16\x66orward_payload_header\x18\x08 \x01(\tB\x17\n\x15jwks_source_specifier\"\x8c\x01\n\nRemoteJwks\x12K\n\x08http_uri\x18\x01 \x01(\x0b\x32\x39.istio.envoy.config.filter.http.jwt_auth.v2alpha1.HttpUri\x12\x31\n\x0e\x63\x61\x63he_duration\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration\"/\n\tJwtHeader\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0cvalue_prefix\x18\x02 \x01(\t\"\xd5\x01\n\x11JwtAuthentication\x12H\n\x05rules\x18\x01 \x03(\x0b\x32\x39.istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtRule\x12\x1f\n\x17\x61llow_missing_or_failed\x18\x02 \x01(\x08\x12U\n\x12\x64ist_uri_whitelist\x18\x03 \x03(\x0b\x32\x39.istio.envoy.config.filter.http.jwt_auth.v2alpha1.HttpUriB9Z7istio.io/api/envoy/config/filter/http/jwt_auth/v2alpha1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_HTTPURI = _descriptor.Descriptor(
  name='HttpUri',
  full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.HttpUri',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.HttpUri.uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cluster', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.HttpUri.cluster', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.HttpUri.timeout', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='http_upstream_type', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.HttpUri.http_upstream_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=141,
  serialized_end=248,
)


_DATASOURCE = _descriptor.Descriptor(
  name='DataSource',
  full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.DataSource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.DataSource.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inline_bytes', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.DataSource.inline_bytes', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inline_string', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.DataSource.inline_string', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='specifier', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.DataSource.specifier',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=250,
  serialized_end=344,
)


_JWTRULE = _descriptor.Descriptor(
  name='JwtRule',
  full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='issuer', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtRule.issuer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='audiences', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtRule.audiences', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_jwks', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtRule.remote_jwks', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_jwks', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtRule.local_jwks', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forward', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtRule.forward', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_headers', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtRule.from_headers', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_params', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtRule.from_params', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forward_payload_header', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtRule.forward_payload_header', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='jwks_source_specifier', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtRule.jwks_source_specifier',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=347,
  serialized_end=738,
)


_REMOTEJWKS = _descriptor.Descriptor(
  name='RemoteJwks',
  full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.RemoteJwks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='http_uri', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.RemoteJwks.http_uri', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cache_duration', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.RemoteJwks.cache_duration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=741,
  serialized_end=881,
)


_JWTHEADER = _descriptor.Descriptor(
  name='JwtHeader',
  full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtHeader.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_prefix', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtHeader.value_prefix', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=883,
  serialized_end=930,
)


_JWTAUTHENTICATION = _descriptor.Descriptor(
  name='JwtAuthentication',
  full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtAuthentication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rules', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtAuthentication.rules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allow_missing_or_failed', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtAuthentication.allow_missing_or_failed', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dist_uri_whitelist', full_name='istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtAuthentication.dist_uri_whitelist', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=933,
  serialized_end=1146,
)

_HTTPURI.fields_by_name['timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_HTTPURI.oneofs_by_name['http_upstream_type'].fields.append(
  _HTTPURI.fields_by_name['cluster'])
_HTTPURI.fields_by_name['cluster'].containing_oneof = _HTTPURI.oneofs_by_name['http_upstream_type']
_DATASOURCE.oneofs_by_name['specifier'].fields.append(
  _DATASOURCE.fields_by_name['filename'])
_DATASOURCE.fields_by_name['filename'].containing_oneof = _DATASOURCE.oneofs_by_name['specifier']
_DATASOURCE.oneofs_by_name['specifier'].fields.append(
  _DATASOURCE.fields_by_name['inline_bytes'])
_DATASOURCE.fields_by_name['inline_bytes'].containing_oneof = _DATASOURCE.oneofs_by_name['specifier']
_DATASOURCE.oneofs_by_name['specifier'].fields.append(
  _DATASOURCE.fields_by_name['inline_string'])
_DATASOURCE.fields_by_name['inline_string'].containing_oneof = _DATASOURCE.oneofs_by_name['specifier']
_JWTRULE.fields_by_name['remote_jwks'].message_type = _REMOTEJWKS
_JWTRULE.fields_by_name['local_jwks'].message_type = _DATASOURCE
_JWTRULE.fields_by_name['from_headers'].message_type = _JWTHEADER
_JWTRULE.oneofs_by_name['jwks_source_specifier'].fields.append(
  _JWTRULE.fields_by_name['remote_jwks'])
_JWTRULE.fields_by_name['remote_jwks'].containing_oneof = _JWTRULE.oneofs_by_name['jwks_source_specifier']
_JWTRULE.oneofs_by_name['jwks_source_specifier'].fields.append(
  _JWTRULE.fields_by_name['local_jwks'])
_JWTRULE.fields_by_name['local_jwks'].containing_oneof = _JWTRULE.oneofs_by_name['jwks_source_specifier']
_REMOTEJWKS.fields_by_name['http_uri'].message_type = _HTTPURI
_REMOTEJWKS.fields_by_name['cache_duration'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_JWTAUTHENTICATION.fields_by_name['rules'].message_type = _JWTRULE
_JWTAUTHENTICATION.fields_by_name['dist_uri_whitelist'].message_type = _HTTPURI
DESCRIPTOR.message_types_by_name['HttpUri'] = _HTTPURI
DESCRIPTOR.message_types_by_name['DataSource'] = _DATASOURCE
DESCRIPTOR.message_types_by_name['JwtRule'] = _JWTRULE
DESCRIPTOR.message_types_by_name['RemoteJwks'] = _REMOTEJWKS
DESCRIPTOR.message_types_by_name['JwtHeader'] = _JWTHEADER
DESCRIPTOR.message_types_by_name['JwtAuthentication'] = _JWTAUTHENTICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HttpUri = _reflection.GeneratedProtocolMessageType('HttpUri', (_message.Message,), dict(
  DESCRIPTOR = _HTTPURI,
  __module__ = 'envoy.config.filter.http.jwt_auth.v2alpha1.config_pb2'
  # @@protoc_insertion_point(class_scope:istio.envoy.config.filter.http.jwt_auth.v2alpha1.HttpUri)
  ))
_sym_db.RegisterMessage(HttpUri)

DataSource = _reflection.GeneratedProtocolMessageType('DataSource', (_message.Message,), dict(
  DESCRIPTOR = _DATASOURCE,
  __module__ = 'envoy.config.filter.http.jwt_auth.v2alpha1.config_pb2'
  # @@protoc_insertion_point(class_scope:istio.envoy.config.filter.http.jwt_auth.v2alpha1.DataSource)
  ))
_sym_db.RegisterMessage(DataSource)

JwtRule = _reflection.GeneratedProtocolMessageType('JwtRule', (_message.Message,), dict(
  DESCRIPTOR = _JWTRULE,
  __module__ = 'envoy.config.filter.http.jwt_auth.v2alpha1.config_pb2'
  # @@protoc_insertion_point(class_scope:istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtRule)
  ))
_sym_db.RegisterMessage(JwtRule)

RemoteJwks = _reflection.GeneratedProtocolMessageType('RemoteJwks', (_message.Message,), dict(
  DESCRIPTOR = _REMOTEJWKS,
  __module__ = 'envoy.config.filter.http.jwt_auth.v2alpha1.config_pb2'
  # @@protoc_insertion_point(class_scope:istio.envoy.config.filter.http.jwt_auth.v2alpha1.RemoteJwks)
  ))
_sym_db.RegisterMessage(RemoteJwks)

JwtHeader = _reflection.GeneratedProtocolMessageType('JwtHeader', (_message.Message,), dict(
  DESCRIPTOR = _JWTHEADER,
  __module__ = 'envoy.config.filter.http.jwt_auth.v2alpha1.config_pb2'
  # @@protoc_insertion_point(class_scope:istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtHeader)
  ))
_sym_db.RegisterMessage(JwtHeader)

JwtAuthentication = _reflection.GeneratedProtocolMessageType('JwtAuthentication', (_message.Message,), dict(
  DESCRIPTOR = _JWTAUTHENTICATION,
  __module__ = 'envoy.config.filter.http.jwt_auth.v2alpha1.config_pb2'
  # @@protoc_insertion_point(class_scope:istio.envoy.config.filter.http.jwt_auth.v2alpha1.JwtAuthentication)
  ))
_sym_db.RegisterMessage(JwtAuthentication)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z7istio.io/api/envoy/config/filter/http/jwt_auth/v2alpha1'))
# @@protoc_insertion_point(module_scope)
