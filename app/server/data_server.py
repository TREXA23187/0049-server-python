#! /usr/bin/env python
# -*- coding: utf-8 -*-
from app import proto


# Implement a derived class that rewrites the interface function in rpc
# The automatically generated grpc file contains one more Servicer than the service name in proto
class FormatData(proto.data_pb2_grpc.FormatDataServicer):
    # Rewrite interface functions. Both input and output are Data types defined in proto
    def DoFormat(self, request, context):
        text = request.text
        return proto.data_pb2.actionresponse(text=text.upper(), age=12,
                                             result=[{"url": "12", "title": "12", "snippets": ["12", "12"]},
                                                     {"url": "12", "title": "12",
                                                      "snippets": ["12", "12"]}])  # Returns an instance
