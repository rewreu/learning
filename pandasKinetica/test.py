import sys
sys.path.append("/Users/zhewu/PycharmProjects/learning/pandasKinetica")
from kdf import kdf
import pandas as pd
import gpudb

conn = gpudb.GPUdb(encoding='BINARY', host="k.yamei.info", port="9191")

# df = kDataFrame(pd.read_csv("./pandasKinetica/template.csv"), conn)

df = kdf(conn)
df.from_pandas(pd.read_csv("./tmp/tmp.test3.csv"))
# df.read_table("est6")

df.to_table("est12",charN_On=True, timeStampColumn="ValidDateTime")
# df.to_table("est9",charN_On=False, timeStampColumn="ValidDateTime")

