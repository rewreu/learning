# import sys
# sys.path.append("/Users/zhewu/PycharmProjects/learning/pandasKinetica")
# from kdf import kdf


# from kdfconn import kdf 
# from kdfconn import kdf
import pandas as pd
import gpudb

conn = gpudb.GPUdb(encoding='BINARY', host="k.yamei.info", port="9191")

# df = kDataFrame(pd.read_csv("./pandasKinetica/template.csv"), conn)

df = kdf(conn)



df.from_pandas(pd.read_csv("./tmp/tmp.test3.csv"))
# df.read_table("est6")

df.to_table("est17",charN_On=True, timeStampColumn="ValidDateTime")
# df.to_table("est9",charN_On=False, timeStampColumn="ValidDateTime")


###############################################################################################
from kdfconn import kdf
import pandas as pd
import numpy as np
import gpudb

conn = gpudb.GPUdb(encoding='BINARY', host="k.yamei.info", port="9191")

# df = kDataFrame(pd.read_csv("./pandasKinetica/template.csv"), conn)

df: kdf = kdf(conn) 

# a = np.random.rand(3,1306)
# df.from_pandas(pd.read_csv("./tmp/tmp.test3.csv"))
# # df = pd.DataFrame(data=a)
# df.from_pandas(pd.DataFrame(data=a,index=np.arange(1, 4),columns=np.arange(1, 1307)))
df.from_pandas(pd.read_csv("./tmp/tmp.test3.csv"))
df.to_table("est39",charN_On=False,appendExistTable=False, clearTableIfExist= True)

###############################################################################################


from kdfconn import kdf
import pandas as pd
import numpy as np
import gpudb

conn = gpudb.GPUdb(encoding='BINARY', host="k.yamei.info", port="9191")

df = kdf(conn) 
df.from_pandas(pd.read_csv("./tmp/tmp.test3.csv"))
df.to_table("est39",charN_On=False,appendExistTable=False, clearTableIfExist= True)

