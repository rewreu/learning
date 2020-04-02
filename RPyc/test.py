ip = "localhost"
import matplotlib.pyplot as plt
import rpyc
import pandas as pd
import io
conn = rpyc.classic.connect(ip)


np = conn.modules.numpy

t = np.arange(256)
sp = np.fft.fft(np.sin(t))
freq = np.fft.fftfreq(t.shape[-1])
plt.plot(freq.tolist(), sp.real.tolist(), freq.tolist(), sp.imag.tolist())
plt.show()

pd2 = conn.modules.pandas

df = pd.read_csv("just.csv")

from io import StringIO
# import StringIO
sdf = StringIO()
bdf = io.BytesIO()
df.to_csv(sdf)
df2 = pd2.DataFrame(sdf)

df3 = pd.read_csv(sdf)