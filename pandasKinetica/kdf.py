import pandas as pd
import numpy as np
import gpudb
import math
class kdf(pd.DataFrame):
    def __init__(self, conn=None):
        super().__init__()
        self.__conn = conn
        self.__TYPE_MAP = { 'int64' :   gpudb.GPUdbRecordColumn._ColumnType.LONG,
                  'int32' :   gpudb.GPUdbRecordColumn._ColumnType.INT,
                  'int16' :   gpudb.GPUdbRecordColumn._ColumnType.INT,
                  'float64' : gpudb.GPUdbRecordColumn._ColumnType.DOUBLE,
                  'float32' : gpudb.GPUdbRecordColumn._ColumnType.FLOAT,
                  'object' :  gpudb.GPUdbRecordColumn._ColumnType.STRING }
    def from_pandas(self, df = None):
        super().__init__(df)
    def _getRecord_unit(self, num_records=1000, offset=0, table_name="table"):
        response = self.__conn.get_records(table_name=table_name,
                                    offset=offset, limit=num_records)
        res_decoded = gpudb.GPUdbRecord.decode_binary_data(response["type_schema"],
                                                        response["records_binary"])
        df_unit = pd.DataFrame(res_decoded)
        return df_unit
    def read_table(self, table_name, num_records=-1, batch_limit=20000):
        """
        num_records is the number of records to fetch.
        batch_limit is the limit each time gpudb API can get, find this limit in gpudb.configure, by default it's 20000.
        """
        if num_records > -1 and num_records<=batch_limit:
            df = self._getRecord_unit(num_records=num_records, offset=0, table_name=table_name)
        else:
            num_records_ = self.__conn.show_table(table_name,options={"get_sizes":"true"})["total_size"]
            num_records = num_records_ if num_records==-1 else min(num_records, num_records_)
            loops = ((num_records - 1) // batch_limit) # get the ceiling of integer division
            df = pd.DataFrame()
            for i in range(loops):
                df = df.append(self._getRecord_unit(num_records=batch_limit, 
                                    offset=i * batch_limit, table_name=table_name))
            df = df.append(self._getRecord_unit(num_records=num_records - loops * batch_limit, 
                                    offset= loops * batch_limit, table_name=table_name))
        super().__init__(df)                   


    def _getcoltype(self, column,charN_On, timeStampColumn):
        
        nullable = True if sum(self[column].isnull())>0 else False
        pdtype = str(self.dtypes[column])
        coltype = [column, self.__TYPE_MAP[pdtype]]
        if pdtype == 'object':
            assert timeStampColumn!=column, 'Only support timestamp as numeric type'
            if charN_On:
                
                maxChar = self[column].astype(str).map(len).max()
                charN = 'char' + str(2**math.ceil(math.log2(maxChar)))
                print("Column {} has type {}, converted to {}".format(column, pdtype,charN))
                coltype.append(charN)
            if nullable: coltype.append('nullable')
        else: # numeric columns
            if column==timeStampColumn: coltype.append('timestamp')
            if nullable: coltype.append('nullable')
        return coltype


    def to_table(self, tableName='tmp', clearTableIfExist=False, charN_On=False, timeStampColumn=None):
        types = []
        if clearTableIfExist:
            self.__conn.clear_table(tableName, options={ 'no_error_if_not_exists':'true' })  
            clearTableIfExist = False
        else:
            clearTableIfExist = self.__conn.has_table(tableName)['table_exists']
        assert clearTableIfExist==False, "table {} exist in database, stop ingestion".format(tableName)

        self._tableTypes = [self._getcoltype(column = column, charN_On=charN_On, timeStampColumn=timeStampColumn) for column in self.columns]
        
        try:
            table = gpudb.GPUdbTable(
                _type=self._tableTypes,
                name=tableName,
                options={
                    "is_replicated": "false"
                },
                db=self.__conn
            )
            print("Table successfully created")
        except gpudb.GPUdbException as e:
            print("Table creation failure: {}".format(str(e)))
            
        i = 0
        while True:
            tdf = self[i:i+20000]
            # only replace nan here, if replaced earlier, the float/double column becomes object
            tdf.replace({pd.np.nan: None},inplace=True) 
            insert_records = tdf.to_records(index=False)
            insert_rows = [ list(x.item()) for x in insert_records ]
            if len(insert_rows)==0: break
            table.insert_records(insert_rows)
            i+=20000
            print("{} rows of data inserted.".format(tdf.shape[0]))

    def test(self):
        print("shape of dataframe: ",self.shape)
        print("top 10 rows of data: \n",self.head(10))





# df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])

# df3 = kDataFrame(df2)

