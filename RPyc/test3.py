import rpyc
ip = "192.168.0.103"
c = rpyc.connect(ip, 18861)
c.root.getm()

