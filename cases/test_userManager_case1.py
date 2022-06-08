# 主要实现用户管理中的测试用例

import unittest
from api.userManager import UserManager
from loguru import logger
from datas.userManager_data import UserManagerData


class TestUserManager(unittest.TestCase):
    user_id = 0

    @classmethod
    def setUpClass(cls) -> None:
        cls.user = UserManager()
        cls.user.login()
        cls.username = UserManagerData.user_case1_data.get('username')
        cls.new_username = UserManagerData.user_case1_data.get('new_username')
        cls.password = UserManagerData.user_case1_data.get('password')

    # 添加管理员：只输入用户名和密码
    def test01_add_user(self):
        # self.password = '123456'
        actual_result = self.user.add_user(self.username, self.password)
        data = actual_result.get('data')
        if data:
            self.user_id = data.get('id')
            TestUserManager.user_id = self.user_id
            logger.info("获取添加管理员的用户ID：{}".format(self.user_id))
        self.assertEqual(0, actual_result['errno'])
        self.assertEqual(self.username, actual_result.get('data').get('username'))

    # 编辑用户：修改的用户名称
    def test02_edit_username(self):
        # new_username = 'testb34'
        actual_result = self.user.edit_user(TestUserManager.user_id, self.new_username, password='123456')
        self.assertEqual(0, actual_result['errno'])
        self.assertEqual(self.new_username, actual_result.get('data').get('username'))

    # 查询用户列表
    def test03_search_user(self):
        actual_result = self.user.search_user()
        # logger.info("查询结果{}".format(actual_result))
        self.assertEqual(0,actual_result['errno'])
        self.assertEqual(self.new_username, actual_result.get('data').get('list')[0].get('username'))

    # 删除用户：删除指定id用户
    def test04_delete_user(self):
        logger.info("这里获取user_id：{}".format(self.user_id))
        actual_result = self.user.delete_user(TestUserManager.user_id, self.username)
        self.assertEqual(0, actual_result['errno'])


if __name__ == '__main__':
    unittest.main()
