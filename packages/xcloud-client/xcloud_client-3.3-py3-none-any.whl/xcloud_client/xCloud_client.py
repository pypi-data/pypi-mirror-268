import jaydebeapi
from pathlib import Path

current_path = Path.cwd()
jar_files =[]
for item in current_path.iterdir():
    if item.suffix =='.jar':
        jar_files.append(item.name)
print(jar_files)
class xCloud_client:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.conn = None

    def connect(self):

        try:
            """
            建立与数据库的连接
            """
            driver = 'com.bonc.xcloud.jdbc.XCloudDriver'
            #com\bonc\xcloud\jdbc
            url = 'jdbc:xcloud:@'+self.host+':'+self.port+'/SERVER_DATA?connectRetry=3&socketTimeOut=43200000&connectDirect=true&buffMemory=33554432'
            #user = config['acct_info']['user']  
            #password = config['acct_info']['password']
            jarFile = [
                '/home/airflow/.local/lib/python3.8/site-packages/xcloud_client/XCloudJDBC-2.10.6.7.jar',
                '/home/airflow/.local/lib/python3.8/site-packages/xcloud_client/slf4j-api-1.7.5.jar',
                '/home/airflow/.local/lib/python3.8/site-packages/xcloud_client/slf4j-log4j12-1.7.5.jar',
                '/home/airflow/.local/lib/python3.8/site-packages/xcloud_client/slf4j-simple-1.7.5.jar',
                '/home/airflow/.local/lib/python3.8/site-packages/xcloud_client/log4j-1.2.17.jar',
                '/home/airflow/.local/lib/python3.8/site-packages/xcloud_client/libthrift-0.9.2.jar',
                '/home/airflow/.local/lib/python3.8/site-packages/xcloud_client/XCloudJDBC_SP_Procedure_Parser-0.1.3.jar',
                '/home/airflow/.local/lib/python3.8/site-packages/xcloud_client/lz4-1.3.0.jar'
           ]
              
            
            print(jarFile)
            conn = jaydebeapi.connect(jclassname=driver, url=url, driver_args=[self.username, self.password], jars=jarFile)
            return conn
        except jaydebeapi.DatabaseError as e:
            print('the connection was not consistent ,because of {e}')
            raise

    def execute_query(self, query):
        """
        执行查询并返回结果
        """
        self.conn = self.connect()
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
        except jaydebeapi.Error as e:
            print(f"Error executing query: {e}")
            raise
        finally:
            if self.conn:
                self.conn.close()
            
        return result
    
    
