from typing import List

import pytest
import yaml

from pythoncode.calc import Calculator


# 使用fixture对计算器进行实例化,作用范围是整个模块
@pytest.fixture(scope='module')
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")


import os

# 通过os.path.dirname获取文件所在目录
yamlfilepath = os.path.dirname(__file__) + "/datas/calc.yml"
# 打开yaml文件读取相加的数
with open(yamlfilepath, encoding='UTF-8') as f:
    # 读取yaml文件中key为add的value值，并赋值给datas
    datas = yaml.safe_load(f)['calcdata']
    # 从读取的datas中获取key值为add_datas的value值,并赋值给adddatas
    adddatas = datas['add']['datas']
    print(adddatas)
    # 从add_datas中获取key值为add_myid的value值，并赋值给addmyid
    addmyid = datas['add']['myid']
    print(addmyid)

# 打开yaml文件读取相除的数
#with open(yamlfilepath, encoding='UTF-8') as f:
    # 读取yaml文件中key为div的value值，并赋值给datas
    #datas = yaml.safe_load(f)['div']
    # 从读取的datas中获取key值为datas的value值,并赋值给divdatas
    divatas = datas['div']['datas']
    print(divatas)
    # 从datas中获取key值为myid的value值，并赋值给divmyid
    divmyid = datas['div']['myid']
    print(divmyid)

# 打开yaml文件读取相减的数
#with open(yamlfilepath, encoding='UTF-8') as f:
    # 读取yaml文件中key为sub的value值，并赋值给datas
    #datas = yaml.safe_load(f)['sub']
    # 从读取的datas中获取key值为datas的value值,并赋值给divdatas
    subdatas = datas['sub']['datas']
    print(subdatas)
    # 从datas中获取key值为myid的value值，并赋值给divmyid
    submyid = datas['sub']['myid']
    print(submyid)

# 打开yaml文件读取相减的数
#with open(yamlfilepath, encoding='UTF-8') as f:
    # 读取yaml文件中key为sub的value值，并赋值给datas
    #datas = yaml.safe_load(f)['mul']
    # 从读取的datas中获取key值为datas的value值,并赋值给divdatas
    muldatas = datas['mul']['datas']
    print(muldatas)
    # 从datas中获取key值为myid的value值，并赋值给divmyid
    mulmyid = datas['mul']['myid']
    print(mulmyid)


# 使用fixture实现add方法的参数化
@pytest.fixture(params=adddatas, ids=addmyid)
def get_adddata(request):
    data = request.param
    print(f"request.param add的测试数据是：{data}")
    return data


# 使用fixture实现div方法的参数化
@pytest.fixture(params=divatas, ids=divmyid)
def get_divdata(request):
    data = request.param
    print(f"request.param div的测试数据是：{data}")
    return data


# 使用fixture实现sub方法的参数化
@pytest.fixture(params=subdatas, ids=submyid)
def get_subdata(request):
    data = request.param
    print(f"request.param sub的测试数据是：{data}")
    return data


# 使用fixture实现mul方法的参数化
@pytest.fixture(params=muldatas, ids=mulmyid)
def get_muldata(request):
    data = request.param
    print(f"request.param mul的测试数据是：{data}")
    return data


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """ called after collection has been performed, may filter or re-order
    the items in-place.

    :param _pytest.main.Session session: the pytest session object
    :param _pytest.config.Config config: pytest config object
    :param List[_pytest.nodes.Item] items: list of item objects
    """
    print("items")
    print(items)
    # 测试用例反转
    # .reverse()

    # 改写测试用例参数的编码格式
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


def pytest_addoption(parser):  # parser:用户命令行参数与ini文件值的解析器
    mygroup = parser.getgroup("hogwarts")  # 定义一个组，为参数分组,下命所有的option都展示在这个group下
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',  # 默认值
                      dest='dev' or 'st',  # 存储的变量
                      help='set your run env'  # 参数说明
                      )


# 使用fixture获取参数值
@pytest.fixture(scope='session')  # 通过命令行的方式只执行一次
def cmdoption(request):
    return request.config.getoption("--env", default='test')
