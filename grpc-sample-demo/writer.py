import grpc
import item_pb2
import item_pb2_grpc

"""
Sample implementation of a writer that sends a payload to the gRPC server
"""

print("Sending sample payload to gRPC server")

channel = grpc.insecure_channel('localhost:5005')
stub = item_pb2_grpc.ItemServiceStub(channel)

# Update the payload with your own data
item = item_pb2.ItemMessage(
    name="My Item",
    brand_name="My Brand",
    id=123,
    weight=456
)

response = stub.Create(item)