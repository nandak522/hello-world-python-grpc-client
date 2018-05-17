import grpc
from hello_world_python_grpc.service import hello_world_pb2_grpc
from hello_world_python_grpc.service import hello_world_pb2


SERVER_HOST = 'localhost'
SERVER_PORT = '32260'

def main():
    channel = grpc.insecure_channel("{}:{}".format(SERVER_HOST, SERVER_PORT))
    stub = hello_world_pb2_grpc.HelloWorldGreeterStub(channel)
    request = hello_world_pb2.HelloWorldRequest(greeting="Hello World!")
    response = stub.SayHello(request)
    print("Greeter client received: message:" + response.text)


if __name__ == '__main__':
    main()
