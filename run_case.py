import unittest

from HTMLTestRunner import HTMLTestRunner
from api.base import Base

test_report = 'test_report.html'


if __name__ == '__main__':
    # 进行一次登录
    base = Base()
    base.login()
    # 创建套件
    suite = unittest.TestLoader().discover('cases',pattern='test*.py')

    with open(test_report,'wb') as f:

        runner = HTMLTestRunner(f,title='wshop测试报告',description='简化版测试框架')
        runner.run(suite)