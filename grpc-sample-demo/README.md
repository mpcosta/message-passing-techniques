# gRPC Sample Demo
This is a simple app that demonstrates how to use gRPC to create a simple server and client. It also serves as a starter template for users to begin experimenting with writing their own gRPC server and client.

## Generating gRPC files
1. pip install grpcio-tools grpcio
2. python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ item.proto

## Running the app (Server)
1. Run the app: `python main.py`

## Running the payload writer (Client)
1Run the client: `python writer.py`

The application should be available at `127.0.0.1:5005`.
