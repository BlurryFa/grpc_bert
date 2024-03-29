# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import data_pb2 as data__pb2


class Strings2VectorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.StringEncoder = channel.unary_unary(
        '/example.Strings2Vector/StringEncoder',
        request_serializer=data__pb2.Strings.SerializeToString,
        response_deserializer=data__pb2.EncodedVector.FromString,
        )


class Strings2VectorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def StringEncoder(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_Strings2VectorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'StringEncoder': grpc.unary_unary_rpc_method_handler(
          servicer.StringEncoder,
          request_deserializer=data__pb2.Strings.FromString,
          response_serializer=data__pb2.EncodedVector.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'example.Strings2Vector', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
