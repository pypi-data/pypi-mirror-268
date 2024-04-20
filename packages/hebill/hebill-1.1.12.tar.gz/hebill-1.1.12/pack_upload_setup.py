# -*- coding: utf-8 -*-
from setuptools import setup
setup(
    name='hebill',
    version='1.1.12',
    description='Python Hebill',
    long_description=open(r'E:\PythonProjects\hebill\hebill\README.MD', encoding='utf-8').read(),
    long_description_content_type='text/plain',
    packages=[
        'hebill',
    ],
    install_requires=[
        'psutil==5.9.8',
        'pillow==10.3.0',
        'requests==2.31.0',
        'wxpython==4.2.1',
        'reportlab==4.1.0',
        'PyMySQL==1.1.0',
        'DBUtils==3.1.0',
    ],
    python_requires='>=3.12',
)
