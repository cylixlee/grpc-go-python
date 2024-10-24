import os
from concurrent.futures import ThreadPoolExecutor

import grpc
from generated.api.hello_pb2 import HelloRequest, HelloResponse
from generated.api.hello_pb2_grpc import (
    HelloServiceServicer,
    add_HelloServiceServicer_to_server,
)
from grpc import RpcContext


class HelloServiceServer(HelloServiceServicer):
    def Hello(self, request: HelloRequest, context: RpcContext) -> HelloResponse:
        print(f'[HelloService] Received request "{request.name}"')
        return HelloResponse(name=request.name, greet="hello")

    def Goodbye(self, request: HelloRequest, context: RpcContext) -> HelloResponse:
        print(f'[HelloService] Received request "{request.name}"')
        return HelloResponse(name=request.name, greet="goodbye")


def main() -> None:
    # create a gRPC server
    server = grpc.server(ThreadPoolExecutor(os.cpu_count() / 2))
    # register services
    add_HelloServiceServicer_to_server(HelloServiceServer(), server)

    try:
        print("gRPC Server Running...")
        # start gRPC server
        server.add_insecure_port("[::]:11451")
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("gRPC Server Shutdown")


if __name__ == "__main__":
    main()
