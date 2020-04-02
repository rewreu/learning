ip = "192.168.0.103"
import rpyc
conn = rpyc.classic.connect(ip)


torch = conn.modules.torch

a = torch.rand(1000).cuda()
rsys = conn.modules.sys

def square(x):
    return x**2
fn = conn.teleport(square)
fn(2)
