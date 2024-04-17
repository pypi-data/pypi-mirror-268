# zhanshop-py

#### 介绍
pip install build # 构建工具
pip3 install twine 发布工具

新建
pyproject.toml
~~~
[project]
name = "zhanshop"
version = "0.0.1"

~~~

setup.cfg
~~~
[metadata]
name = zhanshop
version = 0.0.1

~~~

setup.py
~~~
from setuptools import setup

setup(
    name="zhanshop",
    version="0.0.1"
)

~~~

python3 -m build #开始构建

twine upload --repository-url https://upload.pypi.org/legacy ./*  #发布

