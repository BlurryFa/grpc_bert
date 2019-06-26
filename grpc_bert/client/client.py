
import sys
sys.path.append("../example/gen_py")
import grpc
import data_pb2
import data_pb2_grpc

_HOST = '127.0.0.1'
_PORT = '19999'

def run():
    with grpc.insecure_channel("{0}:{1}".format(_HOST, _PORT)) as channel:
        client = data_pb2_grpc.Strings2VectorStub(channel=channel)
        response = client.StringEncoder(data_pb2.Strings(content='不好', len=100))
    print(response.vector)


if __name__ == '__main__':
    run()