"""
课后作业 1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
 注意： 使用等价类，边界值，因果图等设计测试用例 测试用例中添加断言，验证结果
   灵活使用setup(), teardown() , setup_class(), teardown_class()
"""
import pytest
import yaml

from pythoncode.calc import Calculator

##add方法参数化值的获取
with open('./datas/calc.yml',encoding = 'utf-8') as f:
    # 读取yaml文件中key为add的value值，并赋值给add_datas
    add_datas = yaml.safe_load(f)['add']
    # 从读取的add_datas中获取key值为datas的value值,并赋值给adddatas
    adddatas = add_datas['datas']
    print(adddatas)
    # 从add_datas中获取key值为myid的value值，并赋值给myid
    add_myid = add_datas['myid']
    print(add_myid)
    #add方法读取完成关闭文件，否则下次无法调用yaml.sfe_load函数
    f.close()

##div方法参数化值的获取
with open('./datas/calc.yml') as f:
    # 读取yaml文件中key为add的value值，并赋值给datas
    div_datas = yaml.safe_load(f)['div']
    # 从读取的datas中获取key值为datas的value值,并赋值给adddatas
    divdatas = div_datas['datas']
    print(divdatas)
    # 从datas中获取key值为myid的value值，并赋值给myid
    div_myid = div_datas['myid']
    print(div_myid)
    #关闭文件
   # f.close()



#定义一个测试计算器的类
class TestCalc:

    #定义一个setup_class用于执行开始计算前的准备工作
    def setup_class(self):
        print("开始计算")
        # 实例化计算器
        self.calc = Calculator()

    # 定义一个teardown_class用于结束计算后释放资源
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,expect',adddatas,ids=add_myid)
    def test_add(self,a,b,expect):
        #调用它的相加add()方法
        result = self.calc.add(a,b)
        #如果计算结果为float类型，使用round方法对结果进行四舍五入，保留2位
        if isinstance(result,float):
            result = round(result,2)
        #断言
        assert expect == result


    @pytest.mark.div
    @pytest.mark.parametrize('a,b,expect', divdatas, ids=div_myid)
    def test_div(self,a,b,expect):
        # 调用它的相加div()方法
        r = self.calc.div(a, b)
        # 如果计算结果为float类型，使用round方法对结果进行四舍五入，保留2位
        if isinstance(r, float):
            r = round(r, 2)
        # 断言
        assert expect == r




