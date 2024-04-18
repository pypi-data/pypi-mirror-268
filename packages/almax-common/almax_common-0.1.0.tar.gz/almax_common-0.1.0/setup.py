from setuptools import setup, find_packages

setup(
    name='almax_common',
    version='0.1.0',
    description='A common library with some of my implementations',
    author='AlMax98',
    author_email='alihaider.maqsood@gmail.com',
    packages=find_packages(),
    install_requires=[
        'tkinter',
        'logging',
        'subprocess',
        'reportlab',
        'threading',
        'datetime',
        'os',
        'sys'
    ]
);