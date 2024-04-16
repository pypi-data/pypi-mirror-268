import enumdef
import cffi
import os
import sys
import acp_idl
import pkg_resources
ffi = cffi.FFI()
platform = sys.platform
if (platform == "linux"):
    lib = ffi.dlopen(pkg_resources.resource_filename('pyacp', 'acp_libs/lib/linux/libacp-c.so'))
else:
    lib = ffi.dlopen(pkg_resources.resource_filename('pyacp', 'acp_libs/lib/win/acp-c.dll'))
ffi.cdef("""
         void acp_version(char *version);
         uint64_t acp_client_init(unsigned char device_id, const char *topic);
         uint64_t acp_client_call(uint64_t handler, const char *req, uint64_t req_len, char *resp,uint64_t *resp_len, uint64_t timeout_ms, uint64_t max_retry);
         void acp_client_destroy(uint64_t handler);
         typedef void (*AcpServerCallback)(const char *req, uint64_t req_len, char *resp, uint64_t *resp_len);
         uint64_t acp_server_init(unsigned char device_id, const char *topic, AcpServerCallback callback, uint64_t resp_data_size);
         uint64_t acp_server_run(uint64_t handler);
         uint64_t acp_server_stop(uint64_t handler);
         void acp_server_destroy(uint64_t handler);
         
         typedef void (*AcpSubscriberCallback)(const char *msg, uint64_t msg_len);
         uint64_t acp_subscriber_init(unsigned char device_id, const char *topic, AcpSubscriberCallback callback);
         uint64_t acp_subscriber_listen(uint64_t handler);
         void acp_subscriber_stop_listen(uint64_t handler);
         void acp_subscriber_destroy(uint64_t handler);
         
         uint64_t acp_publisher_init(unsigned char device_id, const char *topic);
         uint64_t acp_publisher_publish(uint64_t handler, const char *msg, uint64_t msg_size);
         bool acp_publisher_hassubscribers(uint64_t handler);
         void acp_publisher_destroy(uint64_t handler);
         """)

def version(version):
    """AI is creating summary for version

    Args:
        version ([str]): [version]
    """
    lib.acp_version(version.encode())

def client_init(device_id,topic):
    """AI is creating summary for client_init

    Args:
        device_id ([int]): [description]
        topic ([str]): [description]
    """
    
    return lib.acp_client_init(device_id,topic.encode())
def client_call(handler, request, response, timeout_ms, max_retry):
    """AI is creating summary for client_call

    Args:
        handler ([int]): [client init return value]
        request ([acp_pb2.Request()]): [client request parameters]
        response ([acp_pb2.Response()]): [server response parameters]
        timeout_ms ([int]): [ms]
        max_retry ([int]): [count]
    """
    req = request.SerializeToString()
    req_len = len(req)
    resp = ffi.new("char[20971520]")  # 分配存储响应的缓冲区20m
    resp_len = ffi.new("uint64_t *")
    ret = lib.acp_client_call(handler, req, req_len, resp, resp_len, timeout_ms, max_retry)
    print(ret)
    if (ret == enumdef.Errors.ACP_ERR_OK):
        print("acp error ok",resp_len[0])
        data_bytes = ffi.buffer(resp, resp_len[0])
        response.parse(data_bytes[:])
        return ret
    return -1
def client_destroy(handler):
    """AI is creating summary for client_destroy

    Args:
        handler ([int]): [client init return value]
    """
    lib.acp_client_destroy(handler)    

def server_init(device_id, topic, server_callback,resp_data_size):
    result = lib.acp_server_init(device_id, topic.encode(), server_callback,resp_data_size)
    return result

def server_run(handle):
    """AI is creating summary for client_destroy

    Args:
        handler ([int]): [server_init return value]
    """
    result = lib.acp_server_run(handle)
    return result

def server_stop(handler):
    """AI is creating summary for client_destroy

    Args:
        handler ([int]): [server_init return value]
    """
    result = lib.acp_server_stop(handler)
    return result
def server_destroy(handler):
    """AI is creating summary for client_destroy

    Args:
        handler ([int]): [server_init return value]
    """
    lib.acp_server_destroy(handler)
    
def subscriber_init(device_id,topic,sub_callback):
    """AI is creating summary for acp_subscriber_init

    Args:
        device_id ([int]): [description]
        topic ([str]): [description]
        sub_callback ([function callback]): [description]
    """
    return lib.acp_subscriber_init(device_id,topic.encode(),sub_callback)
    
def subscriber_listen(handler):
    """AI is creating summary for subscriber_listen

    Args:
        handler ([int]): [subscriber_init return value]

    Returns:
        [int]: [description]
    """
    return lib.acp_subscriber_listen(handler)

def subscriber_stop_listen(handler):
    """AI is creating summary for subscriber_stop_listen

    Args:
        handler ([int]): [subscriber_init return value]
    """
    lib.acp_subscriber_stop_listen(handler)
def subscriber_destroy(handler):
    """AI is creating summary for subscriber_destroy

    Args:
        handler ([int]): [subscriber_init return value]
    """
    lib.acp_subscriber_destroy(handler)

def publisher_init(device_id,topic):
    """AI is creating summary for publisher_init

    Args:
        device_id ([int]): [description]
        topic ([str]): [description]

    Returns:
        [int]: [description]
    """
    return lib.acp_publisher_init(device_id,topic.encode())

def publisher_publish(handler,message):
    """AI is creating summary for publisher_publish

    Args:
        handler ([int]): [publisher_init return value]
        message ([proto type]): [description]
    """
    msg = message.SerializeToString()
    msg_len = len(msg)
    lib.acp_publisher_publish(handler,msg,msg_len)

def publisher_hassubscribers(handler):
    """AI is creating summary for publisher_hassubscribers

    Args:
        handler ([int]): [description]

    Returns:
        [int]: [description]
    """
    return lib.acp_publisher_hassubscribers(handler)

def publisher_destroy(handler):
    """AI is creating summary for publisher_destroy

    Args:
        handler ([int]): [publisher init return value]
    """
    lib.acp_publisher_destroy(handler)


    
    
    