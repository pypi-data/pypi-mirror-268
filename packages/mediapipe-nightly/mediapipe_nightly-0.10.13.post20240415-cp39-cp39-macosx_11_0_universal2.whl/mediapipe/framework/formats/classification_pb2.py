# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/formats/classification.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0mediapipe/framework/formats/classification.proto\x12\tmediapipe\"S\n\x0e\x43lassification\x12\r\n\x05index\x18\x01 \x01(\x05\x12\r\n\x05score\x18\x02 \x01(\x02\x12\r\n\x05label\x18\x03 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x04 \x01(\t\"G\n\x12\x43lassificationList\x12\x31\n\x0e\x63lassification\x18\x01 \x03(\x0b\x32\x19.mediapipe.Classification\"Z\n\x1c\x43lassificationListCollection\x12:\n\x13\x63lassification_list\x18\x01 \x03(\x0b\x32\x1d.mediapipe.ClassificationListB9\n\"com.google.mediapipe.formats.protoB\x13\x43lassificationProto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mediapipe.framework.formats.classification_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.google.mediapipe.formats.protoB\023ClassificationProto'
  _globals['_CLASSIFICATION']._serialized_start=63
  _globals['_CLASSIFICATION']._serialized_end=146
  _globals['_CLASSIFICATIONLIST']._serialized_start=148
  _globals['_CLASSIFICATIONLIST']._serialized_end=219
  _globals['_CLASSIFICATIONLISTCOLLECTION']._serialized_start=221
  _globals['_CLASSIFICATIONLISTCOLLECTION']._serialized_end=311
# @@protoc_insertion_point(module_scope)
