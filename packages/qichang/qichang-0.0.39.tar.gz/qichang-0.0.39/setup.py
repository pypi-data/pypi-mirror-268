from setuptools import setup, find_packages
from qichang import qichang

setup(
    name='qichang',
    version=qichang.__version__,
    author='Qichang Zheng',
    author_email='qichangzheng@uchicago.edu',
    description='A Python library for interacting with various language model APIs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/QichangZheng/qichang.git',
    packages=find_packages(),
    install_requires=[
        'requests',
        'ping3',
        'bs4',
        'tqdm',
        'openai==1.5.0',
        'func_timeout',
    ],
    license='Apache License 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='language models API client',
    python_requires='>=3.7',
)
