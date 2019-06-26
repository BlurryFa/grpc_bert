import sys
sys.path.append('../example/gen_py')
sys.path.append('./bert_utils_master')
import grpc
import time
from concurrent import futures
import data_pb2
import data_pb2_grpc
from bert_utils_master.extract_feature import BertVector

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = "127.0.0.1"
_PORT = "19999"

bert = BertVector()

class StringsToVector(data_pb2_grpc.Strings2VectorServicer):
    def StringEncoder(self, request, context):
        global bert
        if bert is None:
            bert = BertVector()
        content = request.content
        len_of_strings = request.len
        content = content[:len_of_strings]
        vector = bert.encode([content])

        return data_pb2.EncodedVector(vector=vector)

def server():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    data_pb2_grpc.add_Strings2VectorServicer_to_server(StringsToVector(), grpcServer)
    grpcServer.add_insecure_port("{0}:{1}".format(_HOST, _PORT))
    grpcServer.start()

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)

if __name__ == '__main__':
    server()