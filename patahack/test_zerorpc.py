import zerorpc
c = zerorpc.Client()
c.connect("tcp://127.0.0.1:6969")
print(c.hello("RPC"))

