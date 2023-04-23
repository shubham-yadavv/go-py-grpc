from __future__ import print_function
import logging

import grpc

import py_protos.hi_pb2 as hi_pb2
import py_protos.hi_pb2_grpc as hi_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hi_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hi_pb2.HelloRequest(name='world'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()