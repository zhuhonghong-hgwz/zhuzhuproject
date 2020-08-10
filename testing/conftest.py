import pytest
import yaml

from pythoncode.calc import Calculator

#使用fixture对计算器进行实例化,作用范围是整个模块
@pytest.fixture(scope='module')
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")

#打开yaml文件读取相加的数
with open('./datas/calc.yml',encoding = 'UTF-8') as f:
    # 读取yaml文件中key为add的value值，并赋值给datas
    datas = yaml.safe_load(f)['add']
    # 从读取的datas中获取key值为add_datas的value值,并赋值给adddatas
    adddatas = datas['datas']
    print(adddatas)
    # 从add_datas中获取key值为add_myid的value值，并赋值给addmyid
    addmyid = datas['myid']
    print(addmyid)

#打开yaml文件读取相除的数
with open('./datas/calc.yml', encoding='UTF-8') as f:
    # 读取yaml文件中key为div的value值，并赋值给datas
    datas = yaml.safe_load(f)['div']
    # 从读取的datas中获取key值为datas的value值,并赋值给divdatas
    divatas = datas['datas']
    print(divatas)
    # 从datas中获取key值为myid的value值，并赋值给divmyid
    divmyid = datas['myid']
    print(divmyid)

#打开yaml文件读取相减的数
with open('./datas/calc.yml', encoding='UTF-8') as f:
    # 读取yaml文件中key为sub的value值，并赋值给datas
    datas = yaml.safe_load(f)['sub']
    # 从读取的datas中获取key值为datas的value值,并赋值给divdatas
    subdatas = datas['datas']
    print(subdatas)
    # 从datas中获取key值为myid的value值，并赋值给divmyid
    submyid = datas['myid']
    print(submyid)

#打开yaml文件读取相减的数
with open('./datas/calc.yml', encoding='UTF-8') as f:
    # 读取yaml文件中key为sub的value值，并赋值给datas
    datas = yaml.safe_load(f)['mul']
    # 从读取的datas中获取key值为datas的value值,并赋值给divdatas
    muldatas = datas['datas']
    print(muldatas)
    # 从datas中获取key值为myid的value值，并赋值给divmyid
    mulmyid = datas['myid']
    print(mulmyid)

#使用fixture实现add方法的参数化
@pytest.fixture(params=adddatas,ids=addmyid)
def get_adddata(request):
    data=request.param
    print(f"request.param add的测试数据是：{data}")
    return data

#使用fixture实现div方法的参数化
@pytest.fixture(params=divatas,ids=divmyid)
def get_divdata(request):
    data=request.param
    print(f"request.param div的测试数据是：{data}")
    return data

#使用fixture实现sub方法的参数化
@pytest.fixture(params=subdatas,ids=submyid)
def get_subdata(request):
    data=request.param
    print(f"request.param sub的测试数据是：{data}")
    return data

#使用fixture实现mul方法的参数化
@pytest.fixture(params=muldatas,ids=mulmyid)
def get_muldata(request):
    data=request.param
    print(f"request.param mul的测试数据是：{data}")
    return data