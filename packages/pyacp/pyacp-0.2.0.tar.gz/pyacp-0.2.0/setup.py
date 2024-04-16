from setuptools import setup, find_packages

setup(
    name='pyacp',
    version='0.2.0',
    author='Li Meng',
    description='python fastdds acp api',
    packages=['.',"acp_libs/lib/","acp_libs/lib/linux/","acp_libs/lib/win/"],
    package_data={
        'acp_libs/lib/linux/': ['libacp-c.so','libacp-core.so'],  # 包含的文件列表
        'acp_libs/lib/win/' : ['acp-c.dll','acp-core.dll']
    },
    install_requires=[
        'protobuf==3.19.5',
        'cffi==1.15.1',
        'betterproto==1.2.5'
    ],
)       