import pyacp
import acp_idl
from typing import Union
class AcpClient:
    def __init__(self,device_id: Union[int],topic: Union[str]):
        self.__handler = pyacp.client_init(device_id, topic)
    
    @property
    def handler(self):
        return self.__handler
    
    def call(self,request :Union[acp_idl.Request], response:Union[acp_idl.Response],timeout_ms:Union[int],max_retry:Union[int]):
        return pyacp.client_call(self.__handler,request,response,timeout_ms,max_retry)
    
    def destroy(self):
        pyacp.client_destroy(self.__handler)

class AcpServer:
    def __init__(self,device_id: Union[int],topic: Union[str],callback,resp_data_size:Union[int]):
        self.__handler = pyacp.server_init(device_id, topic, callback,resp_data_size)
        
    @property
    def handler(self):
        return self.__handler
    
    def run(self):
        return pyacp.server_run(self.__handler)
        
    def stop(self):
        return pyacp.server_stop(self.__handler)
    
    def destroy(self):
        return pyacp.server_destroy(self.__handler)
    
class AcpSubscriber:
    def __init__(self,device_id: Union[int],topic: Union[str],callback):
        self.__handler = pyacp.subscriber_init(device_id, topic,callback)
    
    @property
    def handler(self):
        return self.__handler
    
    def listen(self):
        return pyacp.subscriber_listen(self.__handler)
    
    def stop(self):
        return pyacp.subscriber_stop_listen(self.__handler)
    
    def destory(self):
        pyacp.subscriber_destroy(self.__handler)
        
class AcpPublisher:
    def __init__(self,device_id: Union[int],topic: Union[str]):
        self.__handler = pyacp.publisher_init(device_id, topic)
    
    @property
    def handler(self):
        return self.__handler
    
    def publish(self,message : Union[acp_idl.Request,acp_idl.Response]):
        return pyacp.publisher_publish(self.__handler,message)
    
    def hassubscribers(self):
        return pyacp.publisher_hassubscribers(self.__handler)
    
    def destroy(self):
        return pyacp.publisher_destroy(self.__handler)