"""
课后作业 1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
 注意： 使用等价类，边界值，因果图等设计测试用例 测试用例中添加断言，验证结果
   灵活使用setup(), teardown() , setup_class(), teardown_class()

pytest fixture使用：
课后作业 1、补全计算器（加减乘除）的测试用例
2、使用fixture，完成加减乘除用例的自动生成
3、修改测试用例的收集规则，执行所有以 check_开头和test_ 开头的测试用例
4、创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
5、将 Fixture 方法存放在conftest.py ，设置scope=module

pytest plugin课后作业
作业1：
1、编写用例顺序：加- 除-减-乘
2、控制测试用例顺序按照【加-减-乘-除】这个顺序执行
作业2【选做】：
1、注册一个命令行参数env，定义分组hogwarts ,将参数 env放在hogwards分组下
2、env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据
"""

import pytest


# 定义一个测试计算器的类
class TestCalc:

    # 定义一个setup_class用于执行开始计算前的准备工作
    # def setup_class(self):
    #     print("开始计算")
    #     # 实例化计算器
    #     self.calc = Calculator()
    #
    # # 定义一个teardown_class用于结束计算后释放资源
    # def teardown_class(self):
    #     print("结束计算")

    # 测试add方法的测试用例
    @pytest.mark.run(order=1)
    def test_add(self, get_calc, get_adddata):
        # 调用它的相加add()方法
        result = get_calc.add(get_adddata[0], get_adddata[1])
        # 如果计算结果为float类型，使用round方法对结果进行四舍五入，保留2位
        if isinstance(result, float):
            result = round(result, 2)
        # 断言
        assert get_adddata[2] == result

    # 测试div方法的测试用例
    @pytest.mark.run(order=4)
    def test_div(self, get_calc, get_divdata):
        # 调用它的相加div()方法
        r = get_calc.div(get_divdata[0], get_divdata[1])
        # 如果计算结果为float类型，使用round方法对结果进行四舍五入，保留2位
        if isinstance(r, float):
            r = round(r, 2)
        # 断言
        assert get_divdata[2] == r

    # 测试sub方法的测试用例
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_subdata):
        # 调用它的相加div()方法
        r = get_calc.sub(get_subdata[0], get_subdata[1])
        # 如果计算结果为float类型，使用round方法对结果进行四舍五入，保留2位
        if isinstance(r, float):
            r = round(r, 2)
        # 断言
        assert get_subdata[2] == r

    # 测试mul方法的测试用例
    @pytest.mark.run(order=3)
    def test_mul(self, get_calc, get_muldata):
        # 调用它的相加div()方法
        r = get_calc.mul(get_muldata[0], get_muldata[1])
        # 如果计算结果为float类型，使用round方法对结果进行四舍五入，保留2位
        if isinstance(r, float):
            r = round(r, 2)
        # 断言
        assert get_muldata[2] == r
