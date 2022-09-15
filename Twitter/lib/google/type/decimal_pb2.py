# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/type/decimal.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x19google/type/decimal.proto\x12\x0bgoogle.type"\x18\n\x07\x44\x65\x63imal\x12\r\n\x05value\x18\x01 \x01(\tBf\n\x0f\x63om.google.typeB\x0c\x44\x65\x63imalProtoP\x01Z:google.golang.org/genproto/googleapis/type/decimal;decimal\xf8\x01\x01\xa2\x02\x03GTPb\x06proto3'
)


_DECIMAL = DESCRIPTOR.message_types_by_name["Decimal"]
Decimal = _reflection.GeneratedProtocolMessageType(
    "Decimal",
    (_message.Message,),
    {
        "DESCRIPTOR": _DECIMAL,
        "__module__": "google.type.decimal_pb2"
        # @@protoc_insertion_point(class_scope:google.type.Decimal)
    },
)
_sym_db.RegisterMessage(Decimal)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\017com.google.typeB\014DecimalProtoP\001Z:google.golang.org/genproto/googleapis/type/decimal;decimal\370\001\001\242\002\003GTP"
    _DECIMAL._serialized_start = 42
    _DECIMAL._serialized_end = 66
# @@protoc_insertion_point(module_scope)
